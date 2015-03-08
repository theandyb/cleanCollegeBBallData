# cleanCollegeBBallData
Clean up college bball data downloaded from NCAA

#System Requirements

sed, python, R, and make

Also need the data.table library in R

#Instructions
1. Get source directory:
	```
	git clone https://github.com/theandyb/cleanCollegeBBallData
	```
2. Download data from [NCAA](http://web1.ncaa.org/stats/StatsSrv/rankings?sportCode=MBB)
	* Selection Division
	* Select reporting week (I would go with through most recent week)
	* For statistic category, use the dropdown list for Team and select "All Statistics"
	* Click Show Report(CSV - Spreadsheet) and save this file into the raw_data directory as all_data.csv
3. Run make from the cleanCollegeBBallData directory
