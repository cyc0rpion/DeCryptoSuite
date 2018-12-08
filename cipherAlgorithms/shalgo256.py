#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#shalgo256
#Nov 3,2018
import hashlib

def calculatehash(filename):
	try:
		filecontent = open(filename,'rb').read()
	except:
		filecontent = filename.encode("utf-8")

	sha25six = hashlib.sha256()
	sha25six.update(filecontent)
	return(sha25six.hexdigest())

def main(filelist,mode):
	files = filelist.split("\n")
	hashes=""
	for i in files:
		hashes += calculatehash(i) +"\n"
	return(hashes)