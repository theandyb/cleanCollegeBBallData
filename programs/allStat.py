fName = "/home/andy/Projects/bball2015/raw_data/all_stat2.csv"
num = 1
outFile = "/home/andy/Projects/bball2015/data/" + str(num) + ".csv"
out = open(outFile,'w')

with open(fName,"r") as f:
	for line in f:
		if not "Reclassifying" in line:
			out.write(line)
		else:
			out.close()
			num += 1
			outFile = "/home/andy/Projects/bball2015/data/" + str(num) + ".csv"
			out = open(outFile,'w')
print("Done!")
