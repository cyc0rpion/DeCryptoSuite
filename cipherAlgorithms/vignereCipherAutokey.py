#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#vignereCipherAutokey
#Oct 1,2018

import cipherAlgorithms

def decrypt(cipher,okey):

    key = okey

    if(len(key)<len(cipher)):

        i=0
        while(len(key)<len(cipher)):
            key+=cipher[i]
            i+=1

        plain=""

    print(key)

    clength = len(cipher)
    i=0
    while(i<clength):
        if(cipher[i].isalpha()):
            plain += cipherAlgorithms.vignereMatrix.main(key[i],cipher[i])
        else:
            plain += cipher[i]

        i+=1

    return(plain)

def main(cipher,mode):
    try:
        if(mode==0):
            var = input("Do you know key value? (y/n) ")

            if(var == 'y' or var == 'Y'):
                key = input("Enter key: ")
                result = decrypt(cipher.upper(),key.upper())
                return(result)

            else:
                return("\nWait for Dictionary attack\n")
        if(mode==1):
            from tkinter import simpledialog,messagebox
            var = messagebox.askyesno("Key?","Do you know Key?")

            if(var == 1):
                key = simpledialog.askstring("Key?","Enter Key:")
                result = decrypt(cipher.upper(),key.upper())
                return(result)
            else:
                fresult = "Wait for Dictionary attack"
                return(fresult)
    except:
        return("Not a valid cipher...")