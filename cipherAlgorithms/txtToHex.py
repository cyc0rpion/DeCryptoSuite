#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#txtToHex
#Oct 11,2018

import binascii	

def decrypt(cipher):
	cipher = cipher.encode("utf-8")
	plain = binascii.hexlify(cipher).decode("utf-8")
	return(plain)

def main(cipher,mode):
	try:
		return(decrypt(cipher))
	except:
		retutn("Not a text string...")
