#!/usr/bin/python
import sys
wordcount = {}
contain_word= 0
current_word= None


for l in sys.stdin:
    l = l.strip()	#Removes whitespace around each word
	word, count = l.split('\t', 1) #Splits up the word and counts
	count = int(count)# Converts each count for the words to an int from an str
    
    if current_word == word:
        wordcount[messages_with_word] = count
        contain_word += 1
    else:
        if current_word != None:
		# For each word we calculate...	
			current_word = word #The current word, listed for output
			wordcount = {} 
            messages_with_word = 0
            message_count = len(wordcount.keys()) #The amount of messages the word is in
            total_count = sum(wordcount.values()) #The times the word occurs in all messages
			if current_word == 'Message':
                total_message_count = message_count
            sum_squares = sum(map(lambda x: (x - mean)**2, wordcount.values())) #Compute Sum of Squares
			
							
			#Computing the minimum of the word counts 
            if message_count < total_message_count:
                minimum = 0
            else:
                minimum = min(wordcount.values())
			
            maximum = max(wordcount.values()) #Compute Maximum of all word counts 
			mean = float(total_count/message_count) #The mean of word counts
			variance = round(float(sum_squares/message_count),1) #Compute Variance of word counts
			
			#Print all necessary Variables for each line
            print ('%s\t%s, %s, %s, %s, %s, %s, %s'% (Word, MessageCount,TotalCount, SumofSquares,
                                                      Min, Max, Mean, Variance))        
            wordcount[messages_with_word] = count
            contain_word += 1
        else:
            current_word = word
            wordcount[messages_with_word] = count
            messages_with_word += 1
 
 #Ham-fisted work around to get the final word to print out...Same code as above 
 if current_word != None:
	# For each word we calculate...	
	current_word = word #The current word, listed for output
	wordcount = {} 
    messages_with_word = 0
    message_count = len(wordcount.keys()) #The amount of messages the word is in
    total_count = sum(wordcount.values()) #The times the word occurs in all messages
	if current_word == 'Message':
        total_message_count = message_count
    sum_squares = sum(map(lambda x: (x - mean)**2, wordcount.values())) #Compute Sum of Squares
			
							
	#Computing the minimum of the word counts 
    if message_count < total_message_count:
        minimum = 0
    else:
        minimum = min(wordcount.values())
			
    maximum = max(wordcount.values()) #Compute Maximum of all word counts 
	mean = float(total_count/message_count) #The mean of word counts
	variance = round(float(sum_squares/message_count),1) #Compute Variance of word counts
			
	#Print all necessary Variables for each line
    print ('%s\t%s, %s, %s, %s, %s, %s, %s'% (word, Message Count,Total Count, Sum of Squares,
                                              Min, Max, Mean, Variance))        
	wordcount[messages_with_word] = count
    contain_word += 1