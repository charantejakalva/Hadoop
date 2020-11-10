#!/usr/bin/env python3
import sys

current_word = None
previous_word = None 
word = None
 
for line in sys.stdin:
    line = line.strip()
    word, filename = line.split("\t", 1)
 
    if current_word == word:
        word_dict[word].add(filename)
    else : 
        if current_word :
            print("%s\t%s" % (current_word,word_dict[current_word]))
        word_dict = dict()
        word_dict[word] = set() 
        word_dict[word].add(filename)
        current_word = word
if current_word == word:
    print ('%s\t%s' % (current_word, word_dict[current_word]))
