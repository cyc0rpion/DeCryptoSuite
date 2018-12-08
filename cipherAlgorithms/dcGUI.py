from tkinter import*
dctop = Tk()
dctop.title("DecryptoSuite")

#Start columns
empcol1 = Label(dctop,text="").grid(column=1) #Left Margin
empcol2 = Label(dctop,text="").grid(column=2) 
 
#Encoding Tab Here
empcol4 = Label(dctop,text="").grid(column=4) 
empcol5 = Label(dctop,text="").grid(column=5) 

#Decryption tab Here
empcol7 = Label(dctop,text="").grid(column=7) 
empcol8 = Label(dctop,text="").grid(column=8)

#Integrity Tab Here
empcol10 = Label(dctop,text="       ").grid(column=10) 
empcol11 = Label(dctop,text="       ").grid(column=11)

#Center Frame Here
empcol34 = Label(dctop,text="",width="3").grid(column=34)

#Right Frame Here
empcol36 = Label(dctop,text="").grid(column=36) #Right Margin
empcol37 = Label(dctop,text="").grid(column=37)

#End Columns

logo = PhotoImage(file="dclogo.png")
logoLabel = Label(dctop,image=logo).grid(row=2,column=11)
decrytosuiteLabel = Label(dctop,text="  DeCryptoSuite  ",fg="blue",height="2",font="Helvetica 22 bold italic").grid(row=2,column=12,columnspan=4)

encodingLabel = Label(dctop,text="Encoding",fg="green",bg="light yellow",height="2",width="15",font="Helvetica 12 bold",bd="4").grid(row=4,column=3) 
decryptionLabel = Label(dctop,text="Decryption",fg="green",bg="light yellow",height="2",width="15",font="Helvetica 12 bold",bd="4").grid(row=4,column=6)
integrityLabel = Label(dctop,text="Integrity",fg="green",bg="light yellow",height="2",width="15",font="Helvetica 12 bold",bd="4").grid(row=4,column=9)


#EncodingRadioButtons
morseButton = Radiobutton(dctop,text="Morse Code",value=1,pady=7,padx=18).grid(row=6,column=3,sticky=W)
base64Button = Radiobutton(dctop,text="Base 64",value=2,pady=7,padx=18).grid(row=7,column=3,sticky=W)

asc2txtButton = Radiobutton(dctop,text="ASCII to Text",value=3,pady=7,padx=18).grid(row=8,column=3,sticky=W)
txt2ascButton = Radiobutton(dctop,text="Text to ASCII",value=4,pady=7,padx=18).grid(row=9,column=3,sticky=W)

hex2txtButton = Radiobutton(dctop,text="Hex to Text",value=5,pady=7,padx=18).grid(row=10,column=3,sticky=W)
txt2hexButton = Radiobutton(dctop,text="Text to Hex",value=6,pady=7,padx=18).grid(row=11,column=3,sticky=W)

bin2txtButton = Radiobutton(dctop,text="Binary to Text",value=7,pady=7,padx=18).grid(row=12,column=3,sticky=W)
txt2binButton = Radiobutton(dctop,text="Text to Binary",value=8,pady=7,padx=18).grid(row=13,column=3,sticky=W)

bin2ascButton = Radiobutton(dctop,text="Binary to ASCII",value=9,pady=7,padx=18).grid(row=14,column=3,sticky=W)
asc2binButton = Radiobutton(dctop,text="ASCII to Binary",value=10,pady=7,padx=18).grid(row=15,column=3,sticky=W)

bin2hexButton = Radiobutton(dctop,text="Binary to Hex",value=11,pady=7,padx=18).grid(row=16,column=3,sticky=W)
hex2binButton = Radiobutton(dctop,text="Hex to Binary",value=12,pady=7,padx=18).grid(row=17,column=3,sticky=W)

hex2ascButton = Radiobutton(dctop,text="Hex to ASCII",value=13,pady=7,padx=18).grid(row=18,column=3,sticky=W)
asc2hexButton = Radiobutton(dctop,text="ASCII to Hex",value=14,pady=7,padx=18).grid(row=19,column=3,sticky=W)

#EncryptionRadioButtons

ceaserCButton = Radiobutton(dctop,text="Ceaser Cipher",value=15,pady=7,padx=18).grid(row=6,column=6,sticky=W)
hillCButton = Radiobutton(dctop,text="Hill Cipher",value=16,pady=7,padx=18).grid(row=7,column=6,sticky=W)
railFenceButton = Radiobutton(dctop,text="Rail Fence Cipher",value=17,pady=7,padx=18).grid(row=8,column=6,sticky=W)

vignereCButton = Radiobutton(dctop,text="Vignere Cipher",value=18,pady=7,padx=18).grid(row=9,column=6,sticky=W)
vignereMatrixButton = Radiobutton(dctop,text="Vignere Matrix",value=19,pady=7,padx=18).grid(row=10,column=6,sticky=W)
vignereAutoButton = Radiobutton(dctop,text="Vignere Autokey",value=20,pady=7,padx=18).grid(row=11,column=6,sticky=W)
vernamButton = Radiobutton(dctop,text="Vernam Cipher",value=21,pady=7,padx=18).grid(row=12,column=6,sticky=W)

rowTButton = Radiobutton(dctop,text="Row Trans Cipher",value=22,pady=7,padx=18).grid(row=13,column=6,sticky=W)
colTButton = Radiobutton(dctop,text="Col Trans Cipher",value=23,pady=7,padx=18).grid(row=14,column=6,sticky=W)

#IntegrityRadioButtons

md2Button = Radiobutton(dctop,text="MD2",value=24,pady=7,padx=18).grid(row=6,column=9,sticky=W)
md4Button = Radiobutton(dctop,text="MD4",value=25,pady=7,padx=18).grid(row=7,column=9,sticky=W)
md5Button = Radiobutton(dctop,text="MD5",value=26,pady=7,padx=18).grid(row=8,column=9,sticky=W)
sha1Button = Radiobutton(dctop,text="SHA-1",value=27,pady=7,padx=18).grid(row=9,column=9,sticky=W)
sha2Button = Radiobutton(dctop,text="SHA-2",value=28,pady=7,padx=18).grid(row=10,column=9,sticky=W)
sha256Button = Radiobutton(dctop,text="SHA-256",value=29,pady=7,padx=18).grid(row=11,column=9,sticky=W)
sha384Button = Radiobutton(dctop,text="SHA-384",value=30,pady=7,padx=18).grid(row=12,column=9,sticky=W)

centerFrame = Frame(height="550",width="550",relief=SUNKEN,bd="4").grid(row=4,column=13,columnspan=20,rowspan=17,sticky=W)
empcol34 = Label(dctop,text="",width="3").grid(column=34)
rightFrame = Frame(height="550",width="190",relief=SUNKEN,bd="4").grid(row=4,column=35,rowspan=17,sticky=W)


#CipherTextLabel
#cipherTextLabel = Label(centerFrame,text="CIPHER TEXT",fg="black",font="Helvetica 16 bold",height="2").pack()
#cipherTextField
#cipherTextText = Text(dctop,height="10",width="50",bd="4").grid(row=5,column=15,rowspan=10,columnspan=10,sticky=N)


#CipherTextLabel
#plainTextLabel = Label(dctop,text="PLAIN TEXT",fg="black",font="Helvetica 16 bold",height="2").grid(row=12,column=15,sticky=W)
#cipherTextField
#plainTextText = Text(dctop,height="10",width="50",bd="4").grid(row=13,column=15,rowspan=10,columnspan=10,sticky=N)

#DecryptButton
#decryptButton = Button(dctop,height="1",width="9",text="DECRYPT",font="Helvetica 14 italic",bg="yellow",activebackground="orange",relief=RAISED).grid(row=11,column=16,sticky=W,pady=2)


dctop.mainloop()