#!/usr/bin/python
import sys
import re
#For each line of the imported data set...
for l in sys.stdin:
	#Strip the blank space from the sides
    l = l.strip() 
	#Then for each of the following feilds... 
	fields = [ 'From: ', 'To: ', 'Cc: ', 'Bcc: ', 'Message-ID: ']
    for f in fields:
        l = l.replace(f, '') #Remove the feild from the line replacing with a blank space
	#Then split the line into 5 values and assign each split into a corresponding value 
    id, from_address, to_address, cc_address, bcc_address = line.split('\t',5)
	#The later 4 now become the email keys which are enumerated on (looped over with an automatic counter)
    keys = [from_address, to_address, cc_address, bcc_address]
	#So now for each value within the keys list...
    for k, key in enumerate(keys):
		#Finds all addresses listed under the feilds within the keys list 
        addresses = re.findall('[a-zA-Z\.\/]+\@[a-zA-Z0-9.]+',key) 
		#Then for each one of these addresses...
        for a in addresses: 
            if a == 'NA' or a == '':continue #Skip if its empty
            else:print(fields[k]+a+'\t'+id) #Print adress with feild, sperated by tab         
