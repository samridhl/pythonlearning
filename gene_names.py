#!usr/bin/env python
import fileinput
import json
import re
import sys
 



for line in fileinput.input(['/home/samridhl/data/Homo_sapiens.GRCh37.75.gtf']):	
	if re.match(r'.*\s.*\sgene\s',line):
	 columns = re.split('\t',line)
	 gene_name_matches= re.findall('gene_name \"(.*?)\";',line)
	 if columns[2] == "gene":
	  if gene_name_matches:
 	    print json.dumps({"genename" : gene_name_matches[0], "chr" : columns[0], "startpos" : columns[3], "endpos" : columns[4]})

 	 




