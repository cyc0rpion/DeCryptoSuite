#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#freqAnalysis
#Nov 4,2018
import operator

freq = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
pool = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

def decrypt(cipher):
	ciphertext = cipher
	cipher = cipher.strip()


	for word in cipher:
		if(ord(word)>96 and ord(word)<123):
			pool[word] = int(pool[word])+1

	sorted_pool = sorted(pool.items(), key=operator.itemgetter(1))

	alpha=[]
	beta=[]

	for tup in sorted_pool:
		alpha.append(tup[0])
		beta.append(tup[1])

	alpha.reverse()

	result=""
	i=0
	while(i<len(ciphertext)):
		word = ciphertext[i]
		j=0
		
		while(j<len(alpha)):
			if(word==alpha[j]):
				result += freq[j]
				break
			j+=1

		if(j==len(alpha)):
			result += word
		
		i+=1
	return(result)

def main(cipher):
	try:
		return(decrypt(cipher.lower()))
	except:
		return("String should contain alphabetic characters...")