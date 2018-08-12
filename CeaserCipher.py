# !usr/bin/python

#MohitBalu/DeCryptoSuite
#Cryptanalysis
#CeaserCipher

class CeaserCipher:

    def __init__(self,cipher,shift):
        self.cipher = cipher
        self.shift = shift
        
    def decrypt(self):
        plain=""
        for word in cipher:
            if word == ' ':
                plain = plain + word
            elif  word.isupper():
                plain = plain + chr((ord(word) - shift - 65) % 26 + 65)
            else:
                plain = plain + chr((ord(word) - shift - 97) % 26 + 97)
        return(plain)
         
cipher = input("Enter Cipher Text: ")

var = input("Do you know shift value? (y/n) ")

if(var == 'y' or var == 'Y'):
    shift = int(input("Enter Shift number: "))
    decryption = CeaserCipher(cipher,shift)
    result = decryption.decrypt()
    print(result)
    
else:
    print("\nTrying all shift values...\n")
    for shift in range(1,26):
        decryption = CeaserCipher(cipher,shift)
        result = decryption.decrypt()
        print(result)
    
