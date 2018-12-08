#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#binToTxt
#Oct 13,2018


def decrypt(cipher):
    plain = ""
    chunk = ""
    for word in cipher:
    	if(word != " "):
    		chunk += word
    	else:
    		plain += chr(int(chunk,2))
    		chunk = ""

    plain += chr(int(chunk,2))
    
    return(plain)

def main(cipher,mode):
    try:
        return(decrypt(cipher))
    except:
        return("Not a binary string...")