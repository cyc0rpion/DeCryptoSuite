#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#shalgo1
#Nov 3,2018
import hashlib

def calculatehash(filename):
	try:
		filecontent = open(filename,'rb').read()
	except:
		filecontent = filename.encode("utf-8")

	shaone = hashlib.sha1()
	shaone.update(filecontent)
	return(shaone.hexdigest())

def main(filelist,mode):
	files = filelist.split("\n")
	hashes=""
	for i in files:
		hashes += calculatehash(i)+"\n"
	return(hashes)