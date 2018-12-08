#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#railfenceCipher
#Sep 27,2018

def decrypt(cipher,key):

    plain=""
    length = len(cipher)

    ###Creating a matrix
    matrix = [0] * key
    for i in range(key):
        matrix[i] = [0] * length

    #print(matrix)

    row = 0
    column = 0
    down = 1;
    x = 0
    loop = True
    ###Initializing a matrix
    if(key==2):
        while(x<length):
            matrix[row][column]=1
            row+=1
            column+=1
            x+=1
            if(x>=length):
                break
            matrix[row][column]=1
            row-=1
            column+=1
            x+=1
            
    else:
        while(x<length):
            while(row < key-1):
                matrix[row][column]=1
                row+=1
                column+=1
                x+=1
                #print(matrix)
                #print(x)
                if(x>length-1):
                    loop = False
                    break
            if(loop == False):
                break
            while(row>-1):
                matrix[row][column]=1
                row-=1
                column+=1
                x+=1
                #print(matrix)
                if(x>length-1):
                    loop = False
                    break
            if(loop == False):
                break
    

    #print(matrix)
    ###Creating cipher matrix
    k = 0
    for m in range(key):
        for n in range(length):
            if(matrix[m][n]==1):
                matrix[m][n]= cipher[k]
                k+=1

    ###Reading cipher matrix
    row=0
    column=0
    y=0
    loop = True

    if(key==2):
        while(y<length):
            plain = plain + str(matrix[row][column])
            row+=1
            column+=1
            y+=1
            if(y>=length):
                break
            plain = plain + str(matrix[row][column])
            row-=1
            column+=1
            y+=1
    else:            
        while(y<length):
            while(row<key-1):
                plain = plain + str(matrix[row][column])
                row+=1
                column+=1
                y+=1
                if(y>length-1):
                    loop = False
                    break
            if(loop == False):
                break
            while(row>-1):
                plain = plain + str(matrix[row][column])
                row-=1
                column+=1
                y+=1
                if(y>length-1):
                    loop = False
                    break
            if(loop == False):
                break
          
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
                maxx = int(simpledialog.askstring("Maximum value of Key?","Predict maxiumum key value:"))
                for key in range(1,maxx):
                    result = decrypt(cipher,key)
                    fresult  = fresult + result + "\n";
                return(fresult)
    except:
        return("Not a valid cipher...")