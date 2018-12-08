#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#shalgo224
#Nov 3,2018
import hashlib

def calculatehash(filename):
	try:
		filecontent = open(filename,'rb').read()
	except:
		filecontent = filename.encode("utf-8")

	sha22four = hashlib.sha224()
	sha22four.update(filecontent)
	return(sha22four.hexdigest())

def main(filelist,mode):
	files = filelist.split("\n")
	hashes=""
	for i in files:
		hashes += calculatehash(i) +"\n"
	return(hashes)