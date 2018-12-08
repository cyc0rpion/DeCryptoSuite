#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#ceaserCipher
#Sep 25,2018

def decrypt(cipher,key):
    plain=""
    for word in cipher:
        if(word.isupper()):
            plain = plain + chr((ord(word) - key - 65) % 26 + 65)
        elif(word.islower()):
            plain = plain + chr((ord(word) - key - 97) % 26 + 97)
        else:
            plain += word
    return(plain)

def main(cipher,mode):
    
    if(mode==0):
        var = input("Do you know key? (y/n) ")

        if(var == 'y' or var == 'Y'):
            key = int(input("Enter key: "))
            result = decrypt(cipher,key)
            return(result)

        else:
            print("\nTrying all shift values...\nYou can figure out plain-text\n")
            fresult =""
            for key in range(1,26):
                result = decrypt(cipher,key)
                fresult  = fresult + result + "\n";
            return(fresult)   #return(result) #return to main module to print on terminal or on output file. 
    if(mode==1):
        from tkinter import simpledialog,messagebox
        var = messagebox.askyesno("Key?","Do you know Key?")
        if(var == 1):
            key = int(simpledialog.askstring("Key?","Enter Key:"))
            result = decrypt(cipher,key)
            return(result)
        else:
            fresult = """Trying all shift values...\nYou can figure out plain-text\n"""
            for key in range(1,26):
                result = decrypt(cipher,key)
                fresult  = fresult + result + "\n";
            return(fresult)

