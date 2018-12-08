#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptanalysis
#HillCipher
#Sep 26,2018

import numpy.matlib 
import numpy as np 

        
def decrypt(cipher,mode):

    alpha = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    beta = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

    cipher = cipher.lower()
    plain=""

    if(mode==0):
        opt = input("Do you know key value? y/n :")
        if(opt=="n" or opt=="N"):
            print("Try Dictionary attack")   ################################# Pending Brute Force ###########################
            exit(1)


        rows,columns = input("Hill Cipher uses matrix as a key for encryption.\nEnter no of rows & columns (space separated) for key matrix: ").split()
        rows = int(rows)
        columns = int(columns)


        ###Creating a key matrix
        matrix = [0] * rows
        for i in range(rows):
            matrix[i] = [0] * columns

        values = []
        print("Enter values of key matrix(in row order)")
        eg = """e.g.\t    --          --
                | a   b   c  |
        write   | d   e   f  |    as ->  a b c d e f g h i
                | g   h   i  |
                --          --  \n:"""

        values = input(eg).split()

    if(mode==1):
        from tkinter import simpledialog,messagebox
        var = messagebox.askyesno("Key?","Do you know Key?")
        if(var==0):
            return("Wait for Brute force attack")
        else:
            rowcol = simpledialog.askstring("No of rows & columns?","Hill Cipher uses matrix as a key for encryption.\nEnter number of rows & columns?")
            rows,columns = rowcol.split()
            rows = int(rows)
            columns = int(columns)

            matrix = [0] * rows
            for i in range(rows):
                matrix[i] = [0] * columns

            values = []
            eg = """Enter values of key matrix(in row order)
            e.g.\t    --          --
                | a   b   c  |
        write   | d   e   f  |    as ->  a b c d e f g h i
                | g   h   i  |
                --          --  \n:"""
            values= (simpledialog.askstring("Key?",eg)).split()

    #print(values)

    #Initializing the matrix with key

    k = 0
    for i in range(rows):
        for j in range(columns):
            if(values[k].isalpha()):
                values[k]=alpha[values[k].lower()]
            matrix[i][j]=values[k]
            k+=1

    #print(matrix)

        
    matrix = np.array(matrix, dtype=int)


    #Checking if finite inverse of a matrix exists
    if(np.linalg.det(matrix) == 0 or np.linalg.matrix_rank(matrix) < min(rows,columns)):
        return("Matrix is not invertible. Key matrix is wrong")
                   
    #Inverse of a matrix for decryption
    matrix = np.linalg.inv(matrix)

    #print(matrix)


    #Padding
    length = len(cipher)

    fills = length % rows

    for p in range(rows-fills):
        cipher = cipher + 'z'

    length = len(cipher)
    cipher = list(cipher)

    #print(cipher)
    #print(length)


    #Generating column matrices for multiplying with key matrix
    l_outer = []
    l_inner = []
    m = 0
        
    for k in range(0,length,rows):
        for l in range(0,rows):
            l_inner.append(alpha[cipher[m]])
            m+=1
        l_outer.append(list(l_inner))
        l_inner.clear()

    #print(l_outer)
            
    #Matrix Multiplication

    final =[]
    for x in range(len(l_outer)):
        matrix2 = np.array(l_outer[x]);
        mul = matrix.dot(matrix2)
        final.extend(list(mul))
    
        #print(final)
    result=""


    #mod 26
    for z in range(len(final)):
        #print(z)
        y = int(final[z]) % 26
        #print(y)
        result = result + str(beta[y])

    return(result)


def main(cipher,mode):
    try:
        result = decrypt(cipher,mode)
        return(result)
    except:
        return("Not an inversible matrix...")
