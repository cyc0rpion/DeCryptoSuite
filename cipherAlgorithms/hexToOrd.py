#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#hexToOrd
#Oct 13,2018

import binascii	

def decrypt(cipher):
    plain = ""
    pplain = bytearray.fromhex(cipher).decode()
    for word in pplain:
    	plain += str(ord(word)) + " "

    return(plain)

def main(cipher,mode):
	cipher = cipher.replace(" ","")
	try:
		return(decrypt(cipher))
	except:
		return("Not a hexadecimal string...")

