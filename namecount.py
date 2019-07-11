import os
len_thres = 10
namelistfile = "./glossary/namelist2.txt"
nlf_w = open(namelistfile,"w+",encoding = "utf-8")
namedict = {}
sourcedir = "./source_origin"
ls = os.listdir(sourcedir) 
for i in ls:	
	path = os.path.join(sourcedir,i)
	if os.path.isfile(path):
		f = open(path, "r", encoding="utf-8")
		lines = f.readlines()
		for line in lines:
			if(len(line) <= len_thres):
				if(line in namedict):
					namedict[line] += 1
				else:
					namedict[line] = 0
k = list(namedict.keys())
k.sort(key = lambda x: namedict[x],reverse = True)
for i in k:
	print(namedict[i])
	print(i)
	t = input()
	if(t == "q"):
		break
	if(t == "s"):
		nlf_w.write(i)
		print("saved")