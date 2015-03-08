fDir = "/home/andy/Projects/bball2015/data/"
for i in range(1,32):
	fName = fDir+str(i)+".csv"
	f = open(fName,'r')
	print(str(i)+"\n"+f.readline()+"\n")
	f.close()

