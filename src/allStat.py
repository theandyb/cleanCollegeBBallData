fName = "./raw_data/all_stat2.csv"
num = 1
outFile = "./raw_data/" + str(num) + ".csv"
out = open(outFile,'w')

with open(fName,"r") as f:
	for line in f:
		if not "Reclassifying" in line:
			out.write(line)
		else:
			out.close()
			num += 1
			outFile = "./raw_data/" + str(num) + ".csv"
			out = open(outFile,'w')
print("Done!")
