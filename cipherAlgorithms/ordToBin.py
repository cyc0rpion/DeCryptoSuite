#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#ordToBin
#Oct 13,2018

def decrypt(cipher):
    plain = ""
    chunk = ""
    for word in cipher:
    	if(word != " "):
    		chunk += word
    	else:
    		if(int(chunk)>256):
    			err = "Not an ASCII value: " + chunk + " Exiting..."
    			return(err)
    		
    		plain += "%08d"%int(bin(int(chunk))[2:])
    		plain += " "
    		chunk = ""

    if(int(chunk)>256):
    			err = "Not an ASCII value: " + chunk + " Exiting..."
    			return(err)

    plain += "%08d"%int(bin(int(chunk))[2:])

    return(plain)

def main(cipher,mode):
    try:
        return(decrypt(cipher))
    except:
        return("Not a ASCII string...")