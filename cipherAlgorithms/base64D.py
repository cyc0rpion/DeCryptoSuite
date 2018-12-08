#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#base64D
#Oct 11,2018

import base64

def decrypt(cipher):
	return((base64.b64decode(cipher + "===")))
	
def main(cipher,mode):
	try:
		return(decrypt(cipher))
	except:
		return("Not a base64 encoded string...")
