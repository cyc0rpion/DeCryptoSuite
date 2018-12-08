#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#vernamCipher
#Oct 2,2018

pool ={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25 }

def sxor(str1, str2):
    return hex(int(str1,16) ^ int(str2,16))

def decrypt(cipher,key):

    if(len(key)!=len(cipher)):
        return("One time pad: Length of key should be equal to length of ciphertext.")

    result = ""
    i=0
    while(i<len(cipher)):
        ans = pool[cipher[i]] ^ pool[key[i]]
        result += chr(ans+65)
        i+=1

    return(result)


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