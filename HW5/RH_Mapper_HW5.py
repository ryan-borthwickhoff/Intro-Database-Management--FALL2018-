#!/usr/bin/python
import sys
# This code creates a dictionary for word counts of each line in the input file 
for l in sys.stdin:
    wordcount = {'Message':0}
	
    l = l.strip().lower() # Removes all unnecessary characters at the front/back of each line 
						  # and then makes the whole line lowercase
	words = l.split() # Splits the line into all of it's individual words
    

	# Loops through the words from the split lines then...
    for w in words:
        if w in wordcount.keys():
			#... adds one to the count if the word exists and
            wordcount[w] += 1
        else:
			#... stores new words with a count of 1
            wordcount[w] = 1
        wordcount['Message'] += 1
    
	# Prints each word with its word count from the dictionary
    for w in wordcount.keys():
        print ('%s\t%s'% (w, wordcount[w]))
