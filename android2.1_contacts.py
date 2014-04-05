#! /usr/bin/python

'''
Code to organize the phone records 
'''

import sys
import re

def extractPhoneRecords(filename):
	
	phoneRecordsExtracted=[]

	#---------Reading the file containing the phone contacts
	f=open(filename,'rU')
	text=f.read()

	#---------Filtering the contacts
	phoneContactsHomevoiceTuple=re.findall('FN:(\w+\W*\s*\w*\W*\w*\W*\w*\W*\w*\W*\w*)TEL;HOME;VOICE:(\d{3}-\d{3}-\d{4,6})',text)
	phoneContactsXvoiceTuple=re.findall('FN:(\w+\W*\s*\w*\W*\w*\W*\w*\W*\w*)TEL;X-VOICE:(\d{3}-\d{3}-\d{4,6})',text)
	phoneContactsTuple=phoneContactsXvoiceTuple+phoneContactsHomevoiceTuple

	
	'''
	#print phoneContactsTuple
	phoneNumbers=0
	for phone in phoneContactsTuple:
		phoneNumbers=phoneNumbers+1
	
	print phoneNumbers
	'''
	
	#--------converting the tuple into a dictionary
	phoneContacts={}
	for contact in phoneContactsTuple:
		(name,cellNumber)=contact
		if cellNumber not in phoneContacts:
			phoneContacts[cellNumber]=name
	
	#-------Sorting the phone records alphabetically
	sortedRecords=sorted(phoneContacts.keys())
	
	'''
	for cellNumber in sortedRecords:
		newCellNumber=cellNumber.replace("-","")
		print newCellNumber+" <---==---> "+ phoneContacts[cellNumber],
		
		'''	
	#-------Storing resulting output in phoneRecordsExtracted List
	for cellNumber in sortedRecords:
		newCellNumber=cellNumber.replace("-","")	
		phoneRecordsExtracted.append(newCellNumber +" <---==---> "+ phoneContacts[cellNumber])
	return phoneRecordsExtracted
	
	
def main():
	records=extractPhoneRecords('00001.vcf')
	joinedRecords=''.join(records)
	joinedRecords=joinedRecords+"\n\n**************By Charles Ng'etich*************\n\t\t*****End*****"	
	print joinedRecords
	
	#----writing the same to a text file
	outputFile=open("ContactList.txt",'w')
	outputFile.write(joinedRecords+"\n")
	outputFile.close()






if __name__=='__main__':
	main()
