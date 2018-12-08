#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#mdigest5
#Nov 3,2018
import hashlib

def calculatehash(filename):
	try:
		filecontent = open(filename,'rb').read()
	except:
		filecontent = filename.encode("utf-8")

	mdfive = hashlib.md5()
	mdfive.update(filecontent)
	return(mdfive.hexdigest())

def main(filelist,mode):
	files = filelist.split("\n")
	hashes=""
	for i in files:
		hashes += calculatehash(i) +"\n"
	return(hashes)