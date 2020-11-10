#!/usr/bin/env python3
import sys 

for line in sys.stdin:  
        trigram,count = line.split('\t',1)
        print("%s\t%s" % (trigram,count))
