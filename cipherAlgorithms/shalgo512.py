#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#shalgo512
#Nov 3,2018
import hashlib

def calculatehash(filename):
	try:
		filecontent = open(filename,'rb').read()
	except:
		filecontent = filename.encode("utf-8")

	sha51two = hashlib.sha512()
	sha51two.update(filecontent)
	return(sha51two.hexdigest())

def main(filelist,mode):
	files = filelist.split("\n")
	hashes=""
	for i in files:
		hashes += calculatehash(i) + "\n"
	return(hashes)