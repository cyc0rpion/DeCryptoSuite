#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#dictionaryAttack
#Nov 4,2018
import enchant
d = enchant.Dict("en_US")

from cipherAlgorithms import *
pool = {15:ceaserCipher,16:hillCipher,17:railfenceCipher,1:morseCode,18:vignereCipher,19:vignereCipherAutokey,20:vernamCipher,21:rowTranspositionCipher,22:columnarTranspositionCipher,2:base64D,4:txtToOrd,3:ordToTxt,5:hexToTxt,6:txtToHex,9:binToOrd,10:ordToBin,7:binToTxt,8:txtToBin,11:binToHex,12:hexToBin,13:hexToOrd,14:ordToHex,24:mdigest5,25:shalgo1,26:shalgo224,27:shalgo256,28:shalgo384,29:shalgo512}

def main(cipher,file,algo):
	if(algo==0):
		raise ValueError("Please choose an algorithm from main window.")
	else:
		if(algo==15 or algo==17 or algo==21 or algo==22):
			ncipher = cipher.split(" ")
			with open(file,"r") as f:
				for line in f:
					line = line.strip()
					if(line.isdigit()):
						nplain = pool[algo].decrypt(ncipher[0],int(line))
						if(d.check(nplain)):
							plain = pool[algo].decrypt(cipher,int(line))
							return(plain + "\nKey: " + line)
				return("Cannot find key!")
		elif(algo==18 or algo==19 or algo==20):
			ncipher = cipher.split(" ")
			with open(file,"r") as f:
				for line in f:
					if(line.isalpha()):
						nplain = pool[algo].decrypt(ncipher[0],line)
						if(d.check(nplain)):
							plain = pool[algo].decrypt(cipher,line)
							return(plain + "\nKey: " + line)
				return("Cannot find key!")
		else:
			return("Dictionary Attack cannot be applied on this algorithm.")
