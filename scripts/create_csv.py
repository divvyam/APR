#!/usr/bin/env python3
import pandas as pd
import sys
import os
# from multiprocessing import Pool



def convert_to_csv(file_name):
	df = pd.read_json(file_name, lines=True)
	df = pd.read_json(file_name)
	out_name = "mag_{}.csv".format(os.path.basename(file_name).split(".json")[0])
	dir_name = os.path.dirname(file_name)
	out_file = os.path.join(dir_name, out_name)
	df.to_csv(out_file)
	del df


if __name__ == "__main__":
	files = [ "../../2007.json",  "../../2008.json",  "../../2009.json",  "../../2010.json",  "../../2012.json",  
	"../../2013.json",  "../../2014.json",  "../../2015.json",  "../../2016.json",  "../../2017.json" ]
	# p = Pool(len(files))
	# p.map(convert_to_csv, files)
	for f in files:
		convert_to_csv(f)


