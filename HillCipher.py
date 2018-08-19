# !usr/bin/python


#MohitBalu/DeCryptoSuite
#Cryptanalysis
#HillCipher

import numpy.matlib 
import numpy as np 

class HillCipher:

    def __init__(self,cipher,rows,columns):
        self.cipher = cipher
        self.rows = rows
        self.columns = columns
        
    def decrypt(self):


        alpha = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        beta = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
        cipher = self.cipher
        cipher = cipher.lower()
        plain=""

        ###Creating a matrix
        matrix = [0] * rows
        for i in range(rows):
            matrix[i] = [0] * columns

        #print(matrix)

        values = []
        values = input("Enter values of key matrix(row wise): ").split()
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
            return("Matrix is not invertible")
                   
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


##########################################
 
cipher = str(input("Enter Cipher Text: "))

rows,columns = input("Hill Cipher uses matrix as a key for encryption.\nEnter no of rows & columns (space separated) for key matrix: ").split()
rows = int(rows)
columns = int(columns)

decryption = HillCipher(cipher,rows,columns)
result = decryption.decrypt()
print(result)
