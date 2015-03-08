import sys,getopt

try:
        opts,args = getopt.getopt(sys.argv[1:], "r",["recursive"])
except getopt.GetoptError:
        print "Lulz"

reclass = False
for o,a in opts:
        if o == "-r":
                reclass = True


fName = "./raw_data/all_stat2.csv"
num = 1
outFile = "./raw_data/" + str(num) + ".csv"
out = open(outFile,'w')

with open(fName,"r") as f:
	for line in f:
		if reclass:
			if not "Reclassifying" in line: 
				if not "NCAA" in line:
					out.write(line)
				else:	
					out.close()
					num += 1
					outFile = "./raw_data/" + str(num) + ".csv"
					out = open(outFile,'w')
		else:
			if not "Reclassifying" in line:
				out.write(line)
			else:
				out.close()
				num += 1
				outFile = "./raw_data/" + str(num) + ".csv"
				out = open(outFile,'w')
out.close()
print("Done!")
