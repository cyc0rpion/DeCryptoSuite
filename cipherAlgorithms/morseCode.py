#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#morseCode
#Sep 30,2018


def decrypt(cipher):
	pool = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','-----':'0','--..--':',','.-.-.-':'.','..--..':'?','-..-.':'/','-....-':'-','-.--.':'(','-.--.-':')','.......':' ','/': ' '}
	plain=""
	text=""
	prev=""

	for word in cipher:
		if(word != ' '):
			text += word
			prev=text
		else:
			plain += pool[text]
			text = ""

	plain+=pool[prev]

	return(plain)

def main(cipher,mode): 
	cipher = cipher.lower()
	try:
		result = decrypt(cipher)
		return(result) 
	except:
		return("Not a morse code...")