#!/usr/bin/env python3
import sys
import json
import ast
current_word = None
previous_word = None 
word = None
allcolsdict = dict() 
key = ["name","salary","location","code"]
for line in sys.stdin:
    line = line.strip()
    pkey, values = line.split("\t", 1) 
    if current_word == pkey: 
        res = ast.literal_eval(values) 
        #val = json.loads(values) 
        #print(res)
        (word_dict[pkey]).update(res)
        colstring = ""
        tempdict = word_dict[pkey]
        for i in range(len(tempdict)) : 
            colstring = colstring + "\t" + tempdict[key[i]]
        print("%s\t%s" % (current_word,colstring))
    else : 
        word_dict = dict()
        word_dict[pkey] = dict() 

        res = ast.literal_eval(values) 
        #print(res)
        #val = json.loads(str(values))   
        (word_dict[pkey]).update(res)
        current_word = pkey
 
