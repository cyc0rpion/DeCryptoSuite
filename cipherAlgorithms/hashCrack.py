#!/usr/bin/python
#MohitBalu/DeCryptoSuite
#Cryptography
#hashCrack
#Nov 4,2018

import hashlib

def main(cipher,file,algo):
	if(algo<23 or algo>30):
		return("Please choose correct hashing algorithm!")
	else:
		if(algo==24):
			hashes = cipher.split()
			results=[]
			result="Cannot crack!"
			for onehash in hashes:
				with open(file,'r',encoding='utf-8') as f:
					for cand in f:
						cand = cand.strip()
						itshash = hashlib.md5(cand.encode("utf-8")).hexdigest()
						if(itshash == onehash):
							results.append(cand)
							f.close()
							result=""
							break

			
			for i in results:
				result += i +"\n"
			return(result)

		if(algo==25):
			hashes = cipher.split()
			results=[]
			result="Cannot crack!"
			for onehash in hashes:
				with open(file,'r',encoding='utf-8') as f:
					for cand in f:
						cand = cand.strip()
						itshash = hashlib.sha1(cand.encode("utf-8")).hexdigest()
						if(itshash == onehash):
							results.append(cand)
							f.close()
							result=""
							break

			for i in results:
				result += i +"\n"
			return(result)

		if(algo==26):
			hashes = cipher.split()
			results=[]
			result="Cannot crack!"
			for onehash in hashes:
				with open(file,'r',encoding='utf-8') as f:
					for cand in f:
						cand = cand.strip()
						itshash = hashlib.sha224(cand.encode("utf-8")).hexdigest()
						if(itshash == onehash):
							results.append(cand)
							f.close()
							result=""
							break

			for i in results:
				result += i +"\n"
			return(result)
		if(algo==27):
			hashes = cipher.split()
			results=[]
			result="Cannot crack!"
			for onehash in hashes:
				with open(file,'r',encoding='utf-8') as f:
					for cand in f:
						cand = cand.strip()
						itshash = hashlib.sha256(cand.encode("utf-8")).hexdigest()
						if(itshash == onehash):
							results.append(cand)
							f.close()
							result=""
							break

			for i in results:
				result += i +"\n"
			return(result)
		if(algo==28):
			hashes = cipher.split()
			results=[]
			result="Cannot crack!"
			for onehash in hashes:
				with open(file,'r',encoding='utf-8') as f:
					for cand in f:
						cand = cand.strip()
						itshash = hashlib.sha384(cand.encode("utf-8")).hexdigest()
						if(itshash == onehash):
							results.append(cand)
							f.close()
							result=""
							break

			for i in results:
				result += i +"\n"
			return(result)

		if(algo==29):
			hashes = cipher.split()
			results=[]
			result="Cannot crack!"
			for onehash in hashes:
				with open(file,'r',encoding='utf-8') as f:
					for cand in f:
						cand = cand.strip()
						itshash = hashlib.sha512(cand.encode("utf-8")).hexdigest()
						if(itshash == onehash):
							results.append(cand)
							f.close()
							result=""
							break

			for i in results:
				result += i +"\n"
			return(result)

		else:
			return("Choose correct algorithm!")