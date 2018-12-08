try:
	from tkinter import *
	from functools import partial
	from cipherAlgorithms import *
	from tkinter import simpledialog
	from browse import browse_file
	from tkinter import messagebox

	def call_algo(choice):
		pool = {15:ceaserCipher,16:hillCipher,17:railfenceCipher,1:morseCode,18:vignereCipher,19:vignereCipherAutokey,20:vernamCipher,21:rowTranspositionCipher,22:columnarTranspositionCipher,2:base64D,4:txtToOrd,3:ordToTxt,5:hexToTxt,6:txtToHex,9:binToOrd,10:ordToBin,7:binToTxt,8:txtToBin,11:binToHex,12:hexToBin,13:hexToOrd,14:ordToHex,24:mdigest5,25:shalgo1,26:shalgo224,27:shalgo256,28:shalgo384,29:shalgo512}

		if(choice.get()==0):
			messagebox.showinfo("Choose Algorithm","Please choose algorithm from the main window to decrypt.")
		if(cipherTextText.get("1.0", "end-1c")==""):
			messagebox.showinfo("Empty Cipher Text","Please provide ciphertext to decrypt.")
		else:
			cipher = cipherTextText.get("1.0", "end").strip()
			plain = pool[choice.get()].main(cipher,1)
			plainTextText.delete("1.0",END)
			plainTextText.insert(END,plain)

	def change_labels():
		cipherTextLabel.config(text=" FILE PATH(S)/STRING(S)                                     ")
		plainTextLabel.config(text=" HASH(ES)                                                              ")
		decryptButton.config(text="CALCULATE")

		browseButton.grid(row=1,column=1,sticky=E)

	def restore_labels():
		cipherTextLabel.config(text=" CIPHER TEXT                                                        ")
		plainTextLabel.config(text=" PLAIN TEXT                                                          ")
		decryptButton.config(text="DECRYPT")
		browseButton.grid_forget()

	def select_file():
		fileNames = browse_file()
		cipherTextText.insert(END,fileNames+"\n")

	def launch_freqAna():

		ignore_index=[]

		def kill():
			freq.destroy()

		def analyse():
			ciphertext = cipherText.get("1.0","end-1c")
			plaintext = freqAnalysis.main(ciphertext)
			plainText.delete("1.0",END)
			plainText.insert(END,plaintext)

		def replace_char():
			wholeText = plainText.get("1.0", "end-1c")
			if(wholeText==""):
				#Error Message
				pass
			else:
				r = replaceEntry.get()[0]
				w = withEntry.get()[0]

				newWholeText=""

				i=0
				while(i<len(wholeText)):
					if(i in ignore_index):
						newWholeText += wholeText[i]
					elif(wholeText[i]==r):
						ignore_index.append(i)
						newWholeText +=w
					else:
						newWholeText +=wholeText[i]
					i+=1

				plainText.delete("1.0",END)
				plainText.insert(END,newWholeText)

		freq = Tk()
		freq.title("Frequency Analysis")

		freqLabel = Label(freq,text="DecryptoSuite : Frequency Anaylsis",fg="magenta",font="Helvetica 14 bold")
		freqLabel.grid(row=1,column=1,padx=5,pady=5)

		cipherLabel = Label(freq,text="Paste your cipher text here:",font="Helvetica 12")
		cipherLabel.grid(row=2,column=1,padx=3,pady=3,sticky=W)

		cipherText = Text(freq,height="7",width="50")
		cipherText.grid(row=3,column=1,padx=10,pady=3)
		cipherText.focus_set()

		analyseButton = Button(freq,text="Analyse",width="10",bg="sky blue",font="bold",command=analyse)
		analyseButton.grid(row=4,column=1,padx=10,pady=10)

		resultLabel = Label(freq,text="Result:",font="Helvetica 12")
		resultLabel.grid(row=5,column=1,padx=3,pady=3,sticky=W)

		plainText = Text(freq,height="7",width="50")
		plainText.grid(row=6,column=1,padx=10,pady=3)

		replaceFrame = Frame(freq,relief=SUNKEN,width="500",height="40")
		replaceFrame.grid(row=7,column=1,padx=3,pady=3)

		replaceLabel = Label(replaceFrame,text="Replace: ")
		replaceLabel.grid(row=1,column=1,padx=2,pady=2)

		replaceEntry = Entry(replaceFrame,width=1)
		replaceEntry.grid(row=1,column=2,padx=2,pady=2)

		withLabel = Label(replaceFrame,text="   with: ")
		withLabel.grid(row=1,column=3,padx=2,pady=2)

		withEntry = Entry(replaceFrame,width=1)
		withEntry.grid(row=1,column=4,padx=2,pady=2)

		replaceButton = Button(replaceFrame,text="Replace",font="bold",bg="pink",command=replace_char)
		replaceButton.grid(row=1,column=5,padx=20,pady=2)

		onecharLabel = Label(replaceFrame,text="  *You can replace a character with another character")
		onecharLabel.grid(row=2,column=1,columnspan=6)

		exitButton = Button(freq,text="Exit",width="10",font="bold",command=kill)
		exitButton.grid(row=8,column=1,padx=10,pady=10)

		freq.resizable(0,0)
		freq.mainloop()


	def launch_dictAttack():

		def kill_dic():
			dic.destroy()

		def attack_dic():
			ciphertextdic = cipherTextdic.get("1.0","end-1c")
			plaintext = dictionaryAttack.main(ciphertextdic,filenameEntrydic.get(),choice.get())
			plainTextdic.delete("1.0",END)
			plainTextdic.insert(END,plaintext)

		def select_dict_file():
			fileNames = browse_file()
			filenameEntrydic.insert(END,fileNames)


		dic = Tk()
		dic.title("Dictionary Attack")

		dicLabel = Label(dic,text="DecryptoSuite : Dictionary Attack",fg="magenta",font="Helvetica 14 bold")
		dicLabel.grid(row=1,column=1,padx=5,pady=5)

		cipherLabeldic = Label(dic,text="Paste your cipher text here:",font="Helvetica 12")
		cipherLabeldic.grid(row=2,column=1,padx=3,pady=3,sticky=W)

		cipherTextdic = Text(dic,height="7",width="50")
		cipherTextdic.grid(row=3,column=1,padx=10,pady=3)
		cipherTextdic.focus_set()

		chooseFileFrame = Frame(dic,relief=SUNKEN)
		chooseFileFrame.grid(row=4,column=1,padx=5)

		filenameLabeldic = Label(chooseFileFrame,text="Dictionary File: ",font="Helvetic 12")
		filenameLabeldic.grid(row=1,column=1,sticky=W)

		filenameEntrydic = Entry(chooseFileFrame,bd="2",width="20")
		filenameEntrydic.grid(row=1,column=2)

		browseButtondic = Button(chooseFileFrame,text="Browse",width="10",command=select_dict_file)
		browseButtondic.grid(row=1,column=3,padx=3,pady=3)

		chooseCipheTextLabel = Label(chooseFileFrame,text="*Must choose suitable algorithm from main window",bg="yellow")
		chooseCipheTextLabel.grid(row=2,column=1,columnspan=5,sticky=W)

		attackButtondic = Button(dic,text="Attack",width="10",bg="sky blue",font="bold",command=attack_dic)
		attackButtondic.grid(row=5,column=1,padx=10,pady=10)

		resultLabeldic = Label(dic,text="Result:",font="Helvetica 12")
		resultLabeldic.grid(row=6,column=1,padx=3,pady=3,sticky=W)

		plainTextdic = Text(dic,height="7",width="50")
		plainTextdic.grid(row=7,column=1,padx=10,pady=3)

		exitButtondic = Button(dic,text="Exit",width="10",font="bold",command=kill_dic)
		exitButtondic.grid(row=8,column=1,padx=10,pady=10)

		dic.resizable(0,0)
		dic.mainloop()

	def crack_hashes():

		def kill_crack():
			crack.destroy()

		def crack_me():
			ciphertextcrack = cipherTextcrack.get("1.0","end-1c")
			plaintext = hashCrack.main(ciphertextcrack,filenameEntrycrack.get(),choice.get())
			plainTextcrack.delete("1.0",END)
			plainTextcrack.insert(END,plaintext)

		def select_wordlist_file():
			fileNames = browse_file()
			filenameEntrycrack.insert(END,fileNames)


		crack = Tk()
		crack.title("Hash Cracker")

		crackLabel = Label(crack,text="DecryptoSuite : Hash Cracker",fg="magenta",font="Helvetica 14 bold")
		crackLabel.grid(row=1,column=1,padx=5,pady=5)

		cipherLabelcrack = Label(crack,text="Paste your hashes here:",font="Helvetica 12")
		cipherLabelcrack.grid(row=2,column=1,padx=3,pady=3,sticky=W)

		cipherTextcrack = Text(crack,height="7",width="50")
		cipherTextcrack.grid(row=3,column=1,padx=10,pady=3)
		cipherTextcrack.focus_set()

		wordFileFrame = Frame(crack,relief=SUNKEN)
		wordFileFrame.grid(row=4,column=1,padx=5)

		filenameLabelcrack = Label(wordFileFrame,text="   Wordlist: ",font="Helvetic 12")
		filenameLabelcrack.grid(row=1,column=1,sticky=W)

		filenameEntrycrack = Entry(wordFileFrame,bd="2",width="20")
		filenameEntrycrack.grid(row=1,column=2)

		browseButtoncrack = Button(wordFileFrame,text="Browse",width="10",command=select_wordlist_file)
		browseButtoncrack.grid(row=1,column=3,padx=3,pady=3)

		wordCipherTextLabel = Label(wordFileFrame,text="*Hash crack may take time to crack.",bg="yellow")
		wordCipherTextLabel.grid(row=2,column=1,columnspan=5,sticky=W)

		crackButtoncrack = Button(crack,text="Crack",width="10",bg="sky blue",font="bold",command=crack_me)
		crackButtoncrack.grid(row=5,column=1,padx=10,pady=10)

		resultLabelcrack = Label(crack,text="Result:",font="Helvetica 12")
		resultLabelcrack.grid(row=6,column=1,padx=3,pady=3,sticky=W)

		plainTextcrack = Text(crack,height="7",width="50")
		plainTextcrack.grid(row=7,column=1,padx=10,pady=3)

		exitButtoncrack = Button(crack,text="Exit",width="10",font="bold",command=kill_crack)
		exitButtoncrack.grid(row=8,column=1,padx=10,pady=10)

		crack.resizable(0,0)
		crack.mainloop()

	#Start Root Window Configuration
	dctop = Tk()
	dctop.title("DecryptoSuite")

	#Start Root Window Configuration

	choice = IntVar()

	#Start Columns Definition
	#LeftMargin
	empcol1 = Label(dctop,text="")
	empcol1.grid(column=1)
	empcol2 = Label(dctop,text="")
	empcol2.grid(column=2) 
	#Encoding Tab Here
	empcol4 = Label(dctop,text="")
	empcol4.grid(column=4) 
	empcol5 = Label(dctop,text="")
	empcol5.grid(column=5) 
	#Decryption tab Here
	empcol7 = Label(dctop,text="")
	empcol7.grid(column=7) 
	empcol8 = Label(dctop,text="")
	empcol8.grid(column=8)
	#Integrity Tab Here
	empcol10 = Label(dctop,text="       ")
	empcol10.grid(column=10) 
	empcol11 = Label(dctop,text="       ")
	empcol11.grid(column=11)
	#Center Frame Here
	empcol34 = Label(dctop,text="",width="3")
	empcol34.grid(column=34)
	#Right Frame Here
	empcol36 = Label(dctop,text="")
	empcol36.grid(column=36) #Right Margin
	empcol37 = Label(dctop,text="")
	empcol37.grid(column=37)
	#End Columns Definition

	#Start ToolName Config
	logo = PhotoImage(file="dclogo.png")
	logoLabel = Label(dctop,image=logo)
	logoLabel.grid(row=2,column=11)
	decryptosuiteLabel = Label(dctop,text="  DeCryptoSuite  ",fg="blue",height="1",font="Helvetica 22 bold italic")
	decryptosuiteLabel.grid(row=2,column=12,columnspan=4)
	#End ToolName Config


	#Start OutFrame Config
	#Start TabLabels
	encodingLabel = Label(dctop,text="Encoding",fg="green",bg="light yellow",height="2",width="15",font="Helvetica 12 bold",bd="4")
	encodingLabel.grid(row=4,column=3) 
	decryptionLabel = Label(dctop,text="Decryption",fg="green",bg="light yellow",height="2",width="15",font="Helvetica 12 bold",bd="4")
	decryptionLabel.grid(row=4,column=6)
	hashingLabel = Label(dctop,text="Hashing",fg="green",bg="light yellow",height="2",width="15",font="Helvetica 12 bold",bd="4")
	hashingLabel.grid(row=4,column=9)
	#End TabLables

	#StartEncodingRadioButtons
	morseButton = Radiobutton(dctop,text="Morse Code",value=1,pady=7,padx=18,variable=choice,command=restore_labels)
	morseButton.grid(row=6,column=3,sticky=W)
	base64Button = Radiobutton(dctop,text="Base 64",value=2,pady=7,padx=18,variable=choice,command=restore_labels)
	base64Button.grid(row=7,column=3,sticky=W)
	asc2txtButton = Radiobutton(dctop,text="ASCII to Text",value=3,pady=7,padx=18,variable=choice,command=restore_labels)
	asc2txtButton.grid(row=8,column=3,sticky=W)
	txt2ascButton = Radiobutton(dctop,text="Text to ASCII",value=4,pady=7,padx=18,variable=choice,command=restore_labels)
	txt2ascButton.grid(row=9,column=3,sticky=W)
	hex2txtButton = Radiobutton(dctop,text="Hex to Text",value=5,pady=7,padx=18,variable=choice,command=restore_labels)
	hex2txtButton.grid(row=10,column=3,sticky=W)
	txt2hexButton = Radiobutton(dctop,text="Text to Hex",value=6,pady=7,padx=18,variable=choice,command=restore_labels)
	txt2hexButton.grid(row=11,column=3,sticky=W)
	bin2txtButton = Radiobutton(dctop,text="Binary to Text",value=7,pady=7,padx=18,variable=choice,command=restore_labels)
	bin2txtButton.grid(row=12,column=3,sticky=W)
	txt2binButton = Radiobutton(dctop,text="Text to Binary",value=8,pady=7,padx=18,variable=choice,command=restore_labels)
	txt2binButton.grid(row=13,column=3,sticky=W)
	bin2ascButton = Radiobutton(dctop,text="Binary to ASCII",value=9,pady=7,padx=18,variable=choice,command=restore_labels)
	bin2ascButton.grid(row=14,column=3,sticky=W)
	asc2binButton = Radiobutton(dctop,text="ASCII to Binary",value=10,pady=7,padx=18,variable=choice,command=restore_labels)
	asc2binButton.grid(row=15,column=3,sticky=W)
	bin2hexButton = Radiobutton(dctop,text="Binary to Hex",value=11,pady=7,padx=18,variable=choice,command=restore_labels)
	bin2hexButton.grid(row=16,column=3,sticky=W)
	hex2binButton = Radiobutton(dctop,text="Hex to Binary",value=12,pady=7,padx=18,variable=choice,command=restore_labels)
	hex2binButton.grid(row=17,column=3,sticky=W)
	hex2ascButton = Radiobutton(dctop,text="Hex to ASCII",value=13,pady=7,padx=18,variable=choice,command=restore_labels)
	hex2ascButton.grid(row=18,column=3,sticky=W)
	asc2hexButton = Radiobutton(dctop,text="ASCII to Hex",value=14,pady=7,padx=18,variable=choice,command=restore_labels)
	asc2hexButton.grid(row=19,column=3,sticky=W)
	#EndEncodingRadioButtons

	#StartEncryptionRadioButtons
	ceaserCButton = Radiobutton(dctop,text="Ceaser Cipher",value=15,pady=7,padx=18,variable=choice,command=restore_labels)
	ceaserCButton.grid(row=6,column=6,sticky=W)
	hillCButton = Radiobutton(dctop,text="Hill Cipher",value=16,pady=7,padx=18,variable=choice,command=restore_labels)
	hillCButton.grid(row=7,column=6,sticky=W)
	railFenceButton = Radiobutton(dctop,text="Rail Fence Cipher",value=17,pady=7,padx=18,variable=choice,command=restore_labels)
	railFenceButton.grid(row=8,column=6,sticky=W)
	vignereCButton = Radiobutton(dctop,text="Vignere Cipher",value=18,pady=7,padx=18,variable=choice,command=restore_labels)
	vignereCButton.grid(row=9,column=6,sticky=W)
	vignereAutoButton = Radiobutton(dctop,text="Vignere Autokey",value=19,pady=7,padx=18,variable=choice,command=restore_labels)
	vignereAutoButton.grid(row=10,column=6,sticky=W)
	vernamButton = Radiobutton(dctop,text="Vernam Cipher",value=20,pady=7,padx=18,variable=choice,command=restore_labels)
	vernamButton.grid(row=11,column=6,sticky=W)
	rowTButton = Radiobutton(dctop,text="Row Trans Cipher",value=21,pady=7,padx=18,variable=choice,command=restore_labels)
	rowTButton.grid(row=12,column=6,sticky=W)
	colTButton = Radiobutton(dctop,text="Col Trans Cipher",value=22,pady=7,padx=18,variable=choice,command=restore_labels)
	colTButton.grid(row=13,column=6,sticky=W)
	#EndEncryptionRadioButtons

	#StartIntegrityRadioButtons
	md5Button = Radiobutton(dctop,text="MD5",value=24,pady=7,padx=18,variable=choice,command=change_labels)
	md5Button.grid(row=6,column=9,sticky=W)
	sha1Button = Radiobutton(dctop,text="SHA-1",value=25,pady=7,padx=18,variable=choice,command=change_labels)
	sha1Button.grid(row=7,column=9,sticky=W)
	sha224Button = Radiobutton(dctop,text="SHA-224",value=26,pady=7,padx=18,variable=choice,command=change_labels)
	sha224Button.grid(row=8,column=9,sticky=W)
	sha256Button = Radiobutton(dctop,text="SHA-256",value=27,pady=7,padx=18,variable=choice,command=change_labels)
	sha256Button.grid(row=9,column=9,sticky=W)
	sha384Button = Radiobutton(dctop,text="SHA-384",value=28,pady=7,padx=18,variable=choice,command=change_labels)
	sha384Button.grid(row=10,column=9,sticky=W)
	sha512Button = Radiobutton(dctop,text="SHA-512",value=29,pady=7,padx=18,variable=choice,command=change_labels)
	sha512Button.grid(row=11,column=9,sticky=W)

	#EndIntegrityRadioButtons
	#End OutFrame Config

	#StartInFramesConfig
	centerFrame = Frame(height="550",width="550",relief=SUNKEN)
	centerFrame.grid(row=4,column=13,columnspan=20,rowspan=17,sticky=W)
	empcol34 = Label(dctop,text="",width="3")
	empcol34.grid(column=34)
	rightFrame = Frame(height="550",width="250",relief=SUNKEN,bd="2")
	rightFrame.grid(row=4,column=35,rowspan=17,sticky=W)
	#EndInFramesConfig


	#StartCenterFrameConfig
	#CipherTextLabel
	cipherTextLabel = Label(centerFrame,text=" CIPHER TEXT                                                        ",fg="black",bg="pink",font="Helvetica 16 bold")
	cipherTextLabel.grid(row=1,column=1,sticky=W,padx=2)
	cipherTextText = Text(centerFrame,height="10",width="60",bd="2")
	cipherTextText.grid(row=2,column=1)
	cipherTextText.focus_set()

	browseButton = Button(centerFrame,text="Browse",width="10",command=select_file)

	algo_with_args = partial(call_algo,choice)
	#DecryptButton
	decryptButton = Button(centerFrame,width="10",text="DECRYPT",font="Helvetica 14 bold",bg="yellow",activebackground="yellow",relief=RAISED,command=algo_with_args)
	decryptButton.grid(row=3,column=1,pady=8)

	emprow4 = Label(centerFrame,height="2")
	emprow4.grid(row=4,column=1)
	#PlainTextLabel
	plainTextLabel = Label(centerFrame,text=" PLAIN TEXT                                                           ",fg="black",bg="light green",font="Helvetica 16 bold")
	plainTextLabel.grid(row=5,column=1,sticky=W,padx=2)
	plainTextText = Text(centerFrame,height="10",width="60",bd="2")
	plainTextText.grid(row=6,column=1)
	#ShortcutLabel
	shortcutLabel = Label(centerFrame,text="Shortcut Keys:: Ctrl+K: Cut , Ctrl+Y: Paste")
	shortcutLabel.grid(row=7,column=1,pady=15,sticky=W)
	#EndCenterFrameConfig

	#StartRightFrameConfig
	dontKnowLabel = Label(rightFrame,text="Don't Know Keys? Try these",width="26",height="2",font="Helvetica 12 bold",bg="black",fg="white")
	dontKnowLabel.grid(row=1,column=1)

	freqAnalysisButton = Button(rightFrame,width="18",text="Frequency Analysis",font="Helvetica 14 italic bold",bg="sky blue",relief=RAISED,command=launch_freqAna)
	freqAnalysisButton.grid(row=2,column=1,padx=3,pady=10)

	dictAttackButton = Button(rightFrame,width="18",text="Dictionary Attack",font="Helvetica 14 italic bold",bg="pink",relief=RAISED,command=launch_dictAttack)
	dictAttackButton.grid(row=3,column=1,padx=3,pady=10)

	hashCrackButton = Button(rightFrame,width="18",text="Hash Cracker",font="Helvetica 14 italic bold",bg="yellow",relief=RAISED,command=crack_hashes)
	hashCrackButton.grid(row=4,column=1,padx=3,pady=10)

	emprow4 = Label(rightFrame,height="16")
	emprow4.grid(row=5,column=1)

	copyrightLabel = Label(rightFrame,width="29",text="DeCryptoSuite v0.1 BETA\nDeveloped under Project OFTK\n Contributors: Mohit Balu",bg="black",fg="white")
	copyrightLabel.grid(row=6,column=1)
	#EndRightFrameConfig

	dctop.mainloop()


except (ValueError,TypeError):
    try:
        messagebox.showinfo("Value Error","Please provide correct values. If not resolved mailto: mohit.balu@outlook.com")
    except:
        print("Please provide Correct values in the fields. If not resolved mailto: mohit.balu@outlook.com")

except (IOError,EOFError):
    try:
        messagebox.showinfo("Input Output/File Error","Please check file name and permissions. If not resolved mailto: mohit.balu@outlook.com")
    except:
        print("Please check file names and permissions. If not resolved mailto: mohit.balu@outlook.com")

except (ImportError):
    try:
        messagebox.showinfo("Import Error","Cannot import package/s. Make sure you are using correct version (python3.x), If not resolved mailto: mohit.balu@outlook.com")
    except:
        print("Cannot import package/s. Make sure you are using correct version (python3.x). If not resolved mailto: mohit.balu@outlook.com")

#except:
#    messagebox.showwarning("Error!","An unexpected error has occured. Contact the developer at mohit.balu@outlook.com")
#    try:
#        drimager.destroy()
#    except:
#        pass