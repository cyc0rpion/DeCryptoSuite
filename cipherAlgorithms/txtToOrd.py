#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#txtToOrd
#Oct 11,2018

def decrypt(cipher):
    plain=""
    for word in cipher:
        plain = plain + str(ord(word)) + " "

    return(plain)

def main(cipher,mode):
	try:
		return(decrypt(cipher))
	except:
		return("Not a text string...")