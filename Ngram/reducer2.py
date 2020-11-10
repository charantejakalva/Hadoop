#!/usr/bin/env python3
import sys

current_word = None
current_count = 0 
topten = dict()
for line in sys.stdin:
    line = line.strip()
    
    try : 
        current_word, current_count = line.split('\t', 1)
        current_count = int(current_count)
    except ValueError :
        continue 
    if len(topten) == 10 :
        minvalue = min(topten.values())
        if current_count > minval : 
            minwords = [k for k in topten if topten[k] == minval]
            del topten[minwords[0]]
            topten[current_word]= current_count
    else : 
        topten[current_word]= current_count     
for trigram, count in topten.items():
    print('%s\t%s' % (trigram, count))
