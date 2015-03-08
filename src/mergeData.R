###Note: I don't select all available variables
### To get a list of what variables are in each resulting csv file, run the script
### headers.py

library("data.table")

cols <- list(   c("Name","W","L"),
		c("Name","PTS","PPG","OPP.PTS","OPP.PPG"),
		c("Name", "FGM", "FGA"),
		c("Name", "OPP.FG", "OPP.FGA"),
		c("Name", "X3FG", "X3FGA"),
		c("Name", "Opp.3FGA", "Opp.3FG"),
		c("Name", "FT", "FTA"),
		c("Name", "REB","RPG", "OPP.REB", "OPP.RPG", "REB.MAR"),
		c("Name", "AST", "TO"),
		c("Name", "BLKS", "BKPG"),
		c("Name", "ST"),
		c("Name", "Opp.TO"),
		c("Name", "Fouls"),
		c("Name", "ORebs", "DRebs"))

files <- c(1,4,5,6,8,9,10,11,13,14,15,17,18,21)
fDir <- "./raw_data/"
fName <- paste(fDir, as.character(files[1]),".csv",sep="")
res <- data.table(read.csv(fName)[,cols[[1]]])
setkey(res,Name)

for(i in 2:length(files)){
	#print(i)
	fName <- paste(fDir, as.character(files[i]),".csv",sep="")
	tmp <- data.table(read.csv(fName)[,cols[[i]]])
	setkey(tmp,Name)
	res <- merge(res,tmp,all=TRUE)
	setkey(res,Name)
	#print(res["Alcorn"])
}
write.csv(res,file="./data/final.csv", row.names=FALSE)
