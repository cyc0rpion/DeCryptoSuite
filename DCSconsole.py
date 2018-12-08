#!usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#DCsuiteConsole/mainModule
#Sep 26,2018
try:

    import subprocess
    import argparse
    from cipherAlgorithms import *
    from tkinter import messagebox

    pool = {'ceaser':ceaserCipher,'hill':hillCipher,'railfence':railfenceCipher,'morse':morseCode,'vignere':vignereCipher,'autokey':vignereCipherAutokey,'vernam':vernamCipher,'rowtrans':rowTranspositionCipher,'coltrans':columnarTranspositionCipher,'base64':base64D,'txt2asc':txtToOrd,'asc2txt':ordToTxt,'hex2txt':hexToTxt,'txt2hex':txtToHex,'bin2asc':binToOrd,'asc2bin':ordToBin,'bin2txt':binToTxt,'txt2bin':txtToBin,'bin2hex':binToHex,'hex2bin':hexToBin,'hex2asc':hexToOrd,'asc2hex':ordToHex}

    def decrypt(algorithm,ciphertext):
        return(pool[algorithm].main(ciphertext,0))

    def display_algo():
        #all_algos="""\nYou can use following algorithms with -a/--algorithm option:\nExample: python3 dcsuite.py -a ceaser -c "khoor" -o decrypted.txt\n\nDecoding:\n\t1. Morse Code: morse\n\t2. Base64: base64\n\t3. Binary to ASCII: bin2asc\n\t4. \nSymmetric Ciphers:\n\t1. ceaser : Ceaser Cipher \n\t2. hill : Hill Cipher\n\t3. vignere : Vignere Cipher\n\t4. railfence : Rail Fence Cipher\nAsymmetric Ciphers:\n\t1. rsa : RSA\n\t2. diffie : Diffie Hellman\n\t"""
        all_algos = """
    You can use following algorithms with -a/--algorithm option:

        Decoding & Conversion Algorithms:
        
        1. Morse Code : morse
        2. Base64 : base64
        3. Binary to ASCII : bin2asc
        4. ASCII to Binary : asc2bin
        5. Binary to Text : bin2txt
        6. Text to Binary : txt2bin
        7. ASCII to Text : asc2txt
        8. Text to ASCII : txt2asc
        9. Hex to Text : hex2txt
        10. Text to Hex : txt2hex
        11. Hex to Bin : hex2bin
        12. Bin to Hex : bin2hex
        13. Hex to ASCII : hex2asc
        14. ASCII to Hex : asc2hex

        Decryption Algorithms: 
        
        1. Ceaser Ciphers : ceaser
        2. Vignere (Vignere table) : vignere
        3. Vignere (Autokey) : autokey
        4. Vernam (One time pad) : vernam
        5. Hill Cipher : hill
        6. RailFence Cipher : railfence
        7. Row Transposition : rowtrans
        8. Columnar Transposition : coltrans
            
        Integrity Algorithms:

        1. MD2 : md2
        2. MD4 : md4
        3. MD5 : md5
        4. SHA1 : sha1
        5. SHA256 : sha256
        6. SHA384 : sha384

    Example: python3 dcsuite.py -a base64 -c <"f4de6b4c32"> -o <output.txt>
    """

        return(all_algos)

    def main():

        parser = argparse.ArgumentParser(
            description="""DecryptoSuite v0.1BETA (www.github.com/mohitbalu/DeCryptoSuite/).
    .....................#@@@@@@@@@@@#.....................
    ....................=@#.........#@=....................
    ....................=@#.........#@=....................
    ...........#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#...........
    .........#@@...............................@@#.........
    .........#@@.............@@@@..............@@#.........
    .........#@@.............@...@.............@@#.........
    .........#@@.............@...@.............@@#.........
    .........#@@.............@@@@..............@@#.........
    .........#@....__..__.._._..__..___..___....@#.........
    .........=@...|...|__/.\./.|__\..|../...\...@=.........
    .........-@...|__.|..\..|..|.....|..\___/...@-.........
    ...........#@.............................@#...........
    ...........#@@@#*+......" -"--O "....+*#@@@#...........
    ............#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#............
    ..............+##=..................-=##:..............""",
            epilog= 'Examples: python3 dcsuite.py -a ceaser -c "khoor" -o decrypted.txt'
        )

        parser.add_argument('-a','--algorithm', help = 'Decryption algorithm to be used',metavar='')
        parser.add_argument('-c','--ciphertext', help = 'Cipher text',metavar='')
        parser.add_argument('-if','--inputfile', help='File containing cipher texts',metavar='')
        parser.add_argument('-of','--outputfile', help='File to output the result',metavar='')
        parser.add_argument('-da','--dispalgo', help='Display all the available algorithms',action='store_true')    
        
        args = parser.parse_args()

        #function to display all algorithms
        if(args.dispalgo):
            print(display_algo())

        if(args.algorithm):
            print(decrypt(args.algorithm, args.ciphertext))


    if __name__ == "__main__":
        main()

except (ValueError,TypeError):
    try:
        messagebox.showinfo("Value Error","Please provide correct values.")
    except:
        print("Please provide Correct values in the fields.")

except (IOError,EOFError):
    try:
        messagebox.showinfo("Input Output/File Error","Please check file name and permissions.")
    except:
        print("Please check file names and permissions.")

except (ImportError):
    try:
        messagebox.showinfo("Import Error","Cannot import package/s. Make sure you are using correct version (python3.x)")
    except:
        print("Cannot import package/s. Make sure you are using correct version (python3.x).")

except:
    try:
        messagebox.showwarning("Error!","An unexpected error has occured.")
        drimager.destroy()
    except:
        pass
