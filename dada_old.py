import random
import csv

#following function stolen from Stack Overflow question 3679694
def weighted_choice(choices): #choices any iterateable with 2 items each. choice and weight
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w > r:
         return c
      upto += w
   assert False, "Shouldn't get here"

def how_long(): #returns word length from 1 to 13 letters
	chance = random.random()
	upto = 0
	letters = 0
	while chance > upto and letters < 13:
		letters += 1
		upto += (11.74 * letters ** 3 * 0.4 ** letters) / 100
		#limiting to 13 letters because the above formula = 1 at x = infinity
	return letters
	
#research indicates maximum of 3 vowels in a row, and max 4 consonants
def vowel_letter(): #reserved for future use. return a vowel
	pass
	
def cons_letter(): #reserved for future use. return a consonant
	pass

def dada():	
	two_letter = []
	with open('two_let.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			two_letter.append(row)
	for i in range(len(two_letter)):
		two_letter[i][1] = float(two_letter[i][1])

	general_letter = []		
	with open('gen_let.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			general_letter.append(row)
	for i in range(len(general_letter)):
		general_letter[i][1] = float(general_letter[i][1])
		
	first_letter = []
	with open('first_let.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			first_letter.append(row)
	for i in range(len(first_letter)):
		first_letter[i][1] = float(first_letter[i][1])
	
	word_lengths = [] #array of word lengths
	tweet = "" #output string
	chars_in_tweet = 0 #character counter so it stays a tweet and not a book
		
	while chars_in_tweet < 140:
		length = how_long()
		word_lengths.append(length) 
		chars_in_tweet += (length + 1) #1 for the space
	#can't call how_long() twice because it uses rand()
	
	if chars_in_tweet > 140: 
		word_lengths.pop()

	for i in range(len(word_lengths)):
		if i == len(word_lengths) - 1 and word_lengths[i] > 1:
			tweet += '#'

		if word_lengths[i] == 1:
			if random.random() <= .6486: #research indicates 64.68% of one letter words are a
				a_or_i = 'a'
			else: #the rest are I
				a_or_i = 'I'
			tweet += (a_or_i + ' ')
		elif word_lengths[i] == 2:
			tweet += (weighted_choice(two_letter) + ' ')
		else:
			tweet += weighted_choice(first_letter)
			for k in range (2, word_lengths[i] + 1):
				tweet += weighted_choice(general_letter)
			tweet += ' '
	return tweet