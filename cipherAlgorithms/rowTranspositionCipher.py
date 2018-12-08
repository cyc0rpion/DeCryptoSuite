#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#rowTranspositionCipher
#Oct 2,2018

def decrypt(cipher,key):

    plain=""
    length = len(cipher)

    rows = length//key
    a=rows
    b=length%key

    if(length%key!=0):
        rows+=1

    cols = key

    matrix = [0] * rows
    for i in range(rows):
        matrix[i] = [0] * cols


    if(b!=0):
        e_counts = ((a+1)*key)-length

    k=e_counts

    ttl = rows*cols
    diff = ttl-k
    i=0
    l=0
    while(i<rows):
        j=0
        while(j<cols):
            if(l<diff):
                pass
            else:
                matrix[i][j]=None;
            j+=1
            l+=1
        i+=1

    i=0
    k=0
    while(i<cols):
        j=0
        while(j<rows):
            if(matrix[j][i]!=None):
                matrix[j][i]=cipher[k]
                k+=1
            j+=1
        i+=1

    k=0
    i=0
    while(i<rows):
        j=0
        while(j<cols):
            if(matrix[i][j]!=None):
                plain+=matrix[i][j]
            j+=1
        i+=1

    return(plain)

def main(cipher,mode):
    try:
        if(mode==0):
            var = input("Do you know key value? (y/n) ")

            if(var == 'y' or var == 'Y'):
                key = int(input("Enter Key Value: "))
                result = decrypt(cipher,key)
                return(result)
            else:
                fresult="\n"
                max = int(input("Predict maximum Key value: "))
                for key in range(2,max+1):
                    result = decrypt(cipher,key)
                    fresult += result+"\n"
                return(fresult)
        if(mode==1):
            from tkinter import simpledialog,messagebox
            var = messagebox.askyesno("Key?","Do you know Key?")
            if(var == 1):
                key = int(simpledialog.askstring("Key?","Enter Key:"))
                result = decrypt(cipher,key)
                return(result)
            else:
                fresult="Figure out plaintext from following outputs:"
                maxx = int(simpledialog.askstring("Maximum value of Key?","Predict maximum key value:"))
                for key in range(1,maxx):
                    result = decrypt(cipher,key)
                    fresult  = fresult + result + "\n";
                return(fresult)
    except:
        return("Not a valid cipher...")