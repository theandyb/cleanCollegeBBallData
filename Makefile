data/final.csv: raw_data/all_data2.csv
	Rscript src/mergeData.R

raw_data/all_data2.csv:
	sed '/"Rank"/,/Reclassifying/!d' ./raw_data/all_stat.csv > ./raw_data/all_stat2.csv
	python ./src/allStat.py

clean:
	rm raw_data/all_stat2.csv
	rm raw_data/[0-9]*.csv
