import os
sourcedir = "./source"
namelistfile = "./glossary/namelist.txt"
cmdlistfile = "./glossary/cmdlist.txt"
namelist = []
cmdlist = []
with open(namelistfile,"r",encoding = "utf-8") as f:
	lines = f.readlines()
	for i in lines:
		namelist.append(i.strip())
with open(cmdlistfile,"r",encoding = "utf-8") as f:
	lines = f.readlines()
	for i in lines:
		cmdlist.append(i.strip())
print(namelist)
print(cmdlist)
specialchar = "#"
ls = os.listdir(sourcedir) 


def needbreaker(s):
	ss = s.strip()
	if(ss in namelist or ss in cmdlist or ss == ""):
		return False
	if(ss.endswith(".akb") or ss.endswith(".ogg") or ss.endswith(".vsd") or ss.endswith(".mov") or ss.startswith("/Config")):
		return False
	return True

logfile = open("./sameline.log","w",encoding = "utf-8")
	
for i in ls:
	path = os.path.join(sourcedir,i)
	if os.path.isfile(path):
		dict = {}
		f = open(path, "r", encoding="utf-8")
		lines = f.readlines()
		f_w = open(path, "w", encoding="utf-8")
		for line in lines:
			if(not needbreaker(line)):
				f_w.write(line)
				continue
			if(line in dict):
				dict[line] = dict[line] + 1 
				f_w.write(str(dict[line]) + specialchar + line)
				logfile.write(line)
			else:
				dict[line] = 0
				f_w.write(line)