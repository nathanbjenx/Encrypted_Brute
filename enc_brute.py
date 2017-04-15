#!/usr/bin/env python

import itertools
import os
import commands
import timeit
import math

alternates = [['A','a','@'],['B','b','8'],['C','c'],['D','d'], ['E','e','3'],
['G','g'],['I','i','!'],['J','j'],['K','k'],['L','l','1'],['M','m'],['N','n'],
['O','o','0'],['R','r'],['S','s','5','$'],['U','u']]
dob = ['6-1-1982', '06-01-1982','6-1-82', '06-01-82','6/1/1982', '06/01/1982', '06/01/82', '6/1/82', '6182','611982','06011982',
'3/11/1987', '03/11/1987','03/11/87', '3/11/87','3-11-1987', '03-11/1987', '03-11-87', '31187', '031187', '3111987', '03111987', 
'10-2-2003','10-02-2003', '10-2-03', '10-02-03', '10/2/2003', '10/02/2003', '10/2/2003', '10/2/03', '1022003', '10022003', '10203','100203', 
'15-9-2009', '15-09-2009', '15-09-09', '15-9-09', '15/9/2009', '15/09/2009', '15/09/09', '15/9/09', '1592009', '15092009', '15909', '150909']

def getAlternates(name, names):
	temp = []
	names=[]
	for i in range(len(name)):
		for j in range(len(name[i])):
			temp.append(name[i][j])
	names.append(temp)
	return names

def getPossibleWords(person):
	poss=list(itertools.product(*person))
	return poss

def getWords(possibleWords):
	words=[]
	for i in range(len(possibleWords)):
		word = ""
		for j in range(len(possibleWords[i])):
			word = word + possibleWords[i][j]
		words.append(word)


	return words

def getAlternates(name):
	name = name.lower()
	alt=[]
	for i in range(len(name)):
		for j in range(len(alternates)):
			for k in range(len(alternates[j])):
				if name[i] == alternates[j][k]:
					alt.append(alternates[j])
	return alt

def decrypt(command, fld):
	cmd = command
	output = commands.getstatusoutput(cmd)
	if 'bad' in output[1]:
		print 'Fucked'
		os.system('rm '+fld)
	else:
		print 'We\'ve got a live one'

ben = getWords(getPossibleWords(getAlternates('Ben')))
banks = getWords(getPossibleWords(getAlternates('Banks')))
eleanor = getWords(getPossibleWords(getAlternates('Eleanor')))
imogen = getWords(getPossibleWords(getAlternates('Imogen')))
jude = getWords(getPossibleWords(getAlternates('Jude')))
aidan = getWords(getPossibleWords(getAlternates('Aidan')))
sienna = getWords(getPossibleWords(getAlternates('Sienna')))
alicia = getWords(getPossibleWords(getAlternates('Alicia')))

people=[]

for i in range(len(eleanor)):
	people.append(eleanor[i])
	
for i in range(len(dob)):
	people.append(dob[i])
for i in range(len(alicia)):
	people.append(alicia[i])
for i in range(len(sienna)):
	people.append(sienna[i])
for i in range(len(aidan)):
	people.append(aidan[i])
for i in range(len(jude)):
	people.append(jude[i])
for i in range(len(imogen)):
	people.append(imogen[i])
for i in range(len(banks)):
	people.append(banks[i])
for i in range(len(ben)):
	people.append(ben[i])
	
total = (len(people))*18
combinationCount = 1
fileCount = ['','','']
encryptionType = ['aes-128-cbc','aes-128-ecb','aes-192-cbc','aes-192-ecb','aes-256-cbc','aes-256-ecb']
start_time = timeit.default_timer()

for i in range(len(people)):
	elapsed = timeit.default_timer() - start_time
	if i >0:
		print '\nTime Elapsed: '+str(elapsed) 
		triesPs = (combinationCount)/elapsed
		print 'Approximate Tries per Second: %.2f'%(triesPs)
		seconds = ((total-combinationCount)/triesPs)
		seconds = math.ceil(seconds)
		minutes = (seconds - (seconds % 60))/60
		hours = int((minutes - (minutes %60)) /60)
		minutes = int(minutes - (hours*60))
		seconds = int(seconds - ((hours*3600)+(minutes*60)))
		print 'Approximate Time Remaining: %3d:%02d:%02d'%(hours,minutes,seconds)

	for files in range(len(fileCount)):
		fileNum=files+1
		for enc in range(len(encryptionType)):
			fld = str(fileNum)+'/'+encryptionType[enc]+'/\''+ people[i]+'.zip\''
			cmd='openssl enc -d -'+encryptionType[enc]+' -in 20_'+str(fileNum)+'.enc -out '+fld+' -k '+people[i]
			decrypt(cmd, fld)
			print(str(combinationCount)+' of '+str(total))
			combinationCount+=1	