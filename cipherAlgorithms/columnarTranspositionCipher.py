#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#columnarTranspositionCipher
#Oct 2,2018

def decrypt(cipher,key):

    plain=""
    klength = len(key)
    clength = len(cipher)

    rows = clength//klength
    cols = klength


    if((clength%klength)!=0):
        return("Cipher-text length should be divisible by key length.")

    matrix = [0] * rows
    for i in range(rows):
        matrix[i] = [0] * cols

    key=list(key)

    i=0
    k=1
    while(i<clength):
        upto=i+rows
        chunk = cipher[i:upto]
        x=0
        
        while(x<len(key)):
            if(int(key[x]) == k):
                break
            x+=1
        k+=1
        
        j=0
        while(j<rows):
            matrix[j][x]=chunk[j]
            j+=1

        i+=rows

    i=0
    while(i<rows):
        j=0
        while(j<cols):
            plain+=matrix[i][j]
            j+=1
        i+=1

    return(plain)

def main(cipher,mode):
    try:
        if(mode==0):
            var = input("Do you know key value? (y/n) ")

            if(var == 'y' or var == 'Y'):
                key = (input("Enter Key Value: "))
                result = decrypt(cipher,key)
                return(result)
            else:
                size="Enter size of the key: "
                print("Try Dictionary attack")
        if(mode==1):
            from tkinter import simpledialog,messagebox
            var = messagebox.askyesno("Key?","Do you know Key?")
            if(var == 1):
                key = simpledialog.askstring("Key?","Enter Key:")
                result = decrypt(cipher,key)
                return(result)
            else:
                var2 = messagebox.askyesno("Key Size?","Do you know Key Size?")
                if(var2==0):
                    fresult = "Cannot be decrypted!"
                else:
                    fresult = "Try Dictionary attack..."
            return(fresult)
    except:
        return("Not a valid cipher...")