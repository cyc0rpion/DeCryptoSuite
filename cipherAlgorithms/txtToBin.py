#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#txtToBin
#Oct 13,2018

def decrypt(cipher):
    plain=""
    for word in cipher:
        plain = plain + str("%08d"%int(bin(ord(word))[2:])) + " "

    return(plain)

def main(cipher,mode):
	try:
		return(decrypt(cipher))
	except:
		return("Not a text string...")



