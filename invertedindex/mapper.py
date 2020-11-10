#!/usr/bin/env python3
import sys
import nltk
import re
import os
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stoplist = stopwords.words('english')
ps = PorterStemmer() 

for line in sys.stdin: 
    line = line.strip()
    line = re.sub('[^A-Za-z]+', ' ', line)
    #words = line.split()
    words = [word.lower() for word in line.split() if word not in stoplist]
    for word in words: 
        filepath = os.environ["map_input_file"]
        filename = os.path.split(filepath)[-1]
        print ("%s\t%s" % (word, filename))
 


