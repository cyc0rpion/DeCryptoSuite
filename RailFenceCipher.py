# !usr/bin/python


#MohitBalu/DeCryptoSuite
#Cryptanalysis
#RailFenceCipher

class RailFenceCipher:

    def __init__(self,cipher,key):
        self.cipher = cipher
        self.key = key
        
    def decrypt(self):
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


##########################################
 
cipher = str(input("Enter Cipher Text: "))

var = input("Do you know key value? (y/n) ")

if(var == 'y' or var == 'Y'):
    key = int(input("Enter Key Value: "))
    decryption = RailFenceCipher(cipher,key)
    result = decryption.decrypt()
    print(result)
else:
    max = int(input("Predict maximum Key value: "))
    for key in range(2,max+1):
        decryption = RailFenceCipher(cipher,key)
        result = decryption.decrypt()
        print(result)
