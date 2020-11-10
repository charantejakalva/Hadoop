#!/usr/bin/env python3
import sys 
import os
f1cols = ["name"]
f2cols = ["salary","location","code"]
for line in sys.stdin: 
    line = line.strip()
    key , values = line.split("\t", 1) 
    filepath = os.environ["map_input_file"]
    filename = os.path.split(filepath)[-1]
    if filename == "join1.tsv" : 
        cols= dict()
        colvals = values.split("\t")
        for i in range(len(colvals)) : 
            cols[f1cols[i]] = colvals[i]
    elif filename == "join2.tsv" : 
        cols= dict()
        colvals = values.split("\t")
        for i in range(len(colvals)) : 
            cols[f2cols[i]] = colvals[i]

    print ('%s\t%s' % (key, cols))
 


