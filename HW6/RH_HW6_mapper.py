#!/usr/bin/python
import sys
#For each line of the imported data set...
for l in sys.stdin:
	#Break each line into items, spltting on each tab and removing blank space 
    items = l.strip().split('\t') 

	#For each item from the list of items...
	fields = ('Message-ID', 'From', 'To', 'Cc', 'Bcc') #Look for these feilds
	emails = [] #Then append them to this list
    for i in items:
        if i.startswith(fields): #Looking for the feilds
            emails.append(i) #If there is an item there add the item to the list
    # Now for printing out the items within the feilds...
	#If every feild has an entry, this will print them
    try: print(emails[0]+'\t'+emails[1]+'\t'+emails[2]+'\t'+emails[3]+'\t'+emails[4])
	#If not we figure out which is missing... 
    except IndexError:
        # If the bcc is missing replace with 'NA' then print out eveything else
        try:print(print_items[0]+'\t'+print_items[1]+'\t'+print_items[2]+'\t'+print_items[3]+'\t'+'NA')
        # If the bcc and cc are missing replace with 'NA' then print everything else
        except IndexError:
			print(print_items[0]+'\t'+print_items[1]+'\t'+print_items[2]+'\t'+'NA'+'\t'+'NA')
