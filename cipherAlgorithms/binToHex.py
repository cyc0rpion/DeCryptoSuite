#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#binToHex
#Oct 13,2018

def decrypt(cipher):
    plain = ""
    chunk = ""
    for word in cipher:
    	if(word != " "):
    		chunk += word
    	else:
    		plain += str(hex(int(chunk,2))[2:])
    		chunk = ""

    plain += str(hex(int(chunk,2))[2:])    
    return(plain)

def main(cipher,mode):
    try:
        return(decrypt(cipher))
    except:
        return("Not a binary string...")