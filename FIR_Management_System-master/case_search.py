from calendar import c
import sys,re
import os
#irecord=[]
	#record=open(sys.argv[1]).readlines()

"""def search(txt_file,idx_file,key):
		idx_f=open(idx_file,"r")
		for line in idx_f:
			if re.match(key,line):
				l=line.split()
				n=len(l)
				txt_f=open(sys.argv[1],"r")
				for i in range (1,n):
					c=int(l[i])
					print(record[c-1])
				return l
		idx_f.close()
		search(sys.argv[1],sys.argv[2],sys.argv[3])"""

"""def search(txt_file,idx_file,key):
		idx_f=open(idx_file,"r")
		for line in idx_f:
			if re.match(key,line):
				l=line.split()
				n=len(l)
				txt_f=open(sys.argv[1],"r")
				for i in range (1,n):
					c=int(l[i])
					print(record[c-1])
				return l
				idx_f.close()"""


txt_file="victim.txt"
idx_file="index_file.idx"

#my_list=[txt_file,idx_file]
key=sys.argv[1]


record=[]
record=open(txt_file).readlines()


def search(txt_file,idx_file,key):
	flag=0
	txt_f=open(txt_file,"r")
	for line in txt_f:
		if re.match(key,line):
			flag=1
			l=line.split()
			l1=l[0].split('|')
			print("\nFIR number:"+l1[0])
			print("Victim name:"+l1[1])
			print("Accused name:"+l1[2])
			print("Case date:"+l1[3])
			print("Case time:"+l1[4])
			print("Case description:"+l1[5])

	if(flag==0):
		print("No such record exist")
	txt_f.close()


search(txt_file,idx_file,key)
