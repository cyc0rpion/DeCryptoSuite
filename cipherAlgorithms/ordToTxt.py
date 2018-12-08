#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#ordToTxt
#Oct 11,2018

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
    return(plain)

def main(cipher,mode):
    try:
        return(decrypt(cipher))
    except:
        return("Not a ASCII string...")



