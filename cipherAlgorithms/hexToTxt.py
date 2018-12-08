#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#hexToTxt
#Oct 11,2018

import binascii	

def decrypt(cipher):
    
    plain = binascii.unhexlify(cipher).decode("utf-8")
    return(plain)

def main(cipher,mode):
	cipher = cipher.replace(" ","")
	try:
		return(decrypt(cipher))
	except:
		return("Not a hexadecimal string...")
