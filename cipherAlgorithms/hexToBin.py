#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#hexToBin
#Oct 13,2018

import binascii	

def decrypt(cipher):

	plain = ""

	cipher = cipher.strip()
	tcipher = binascii.unhexlify(cipher).decode("utf-8")

	for word in tcipher:
		plain += str("%08d"%int(bin(ord(word))[2:])) + " "
	
	return(plain)

def main(cipher,mode):
	try:
		return(decrypt(cipher))
	except:
		return("Not a hexadecimal string...")
