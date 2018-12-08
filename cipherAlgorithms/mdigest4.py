#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#mdigest4
#Nov 3,2018
import hashlib

def calculatehash(filename):
	filecontent = open(filename,'rb').read()
	mdfour = hashlib.md4()
	mdfour.update(filecontent)
	return(mdfour.hexdigest()+"\n")

def main(filelist,mode):
	files = filelist.split("\n")
	hashes=""
	for i in files:
		hashes += calculatehash(i)
	return(hashes)