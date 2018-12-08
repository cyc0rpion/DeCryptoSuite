#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#binToOrd
#Oct 11,2018

def decrypt(cipher):
    plain = ""
    chunk = ""
    for word in cipher:
    	if(word != " "):
    		chunk += word
    	else:
    		plain += str(int(chunk,2))
    		plain += " "
    		chunk = ""

    plain += str(int(chunk,2))
    
    return(plain)

def main(cipher,mode):
    try:
        return(decrypt(cipher))
    except:
        return("Not a binary string...")