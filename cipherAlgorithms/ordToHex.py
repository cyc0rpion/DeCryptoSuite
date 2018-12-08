#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#ordToHex
#Oct 13,2018

import binascii

def decrypt(cipher):
    plain=""
    chunk=0
    pchunk=""

    for word in cipher:
    	if(word!=" "):
    		chunk = chunk*10 + int(word)
    
    	else:
    		plain = plain + chr(chunk)
    		chunk=0

    plain += chr(int(chunk))
    plain = plain.encode("utf-8")
    plain = (binascii.hexlify(plain)).decode("utf-8")
    return(plain)

def main(cipher,mode):
    try:
        return(decrypt(cipher))
    except:
        retutn("Not a ASCII string...")



