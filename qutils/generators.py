# qutils.generators

from .__init__ import *
from .creators import email as create_email
import random

def code(length):
	"""Generate a random string from alphabet characters and 0-9 numbers, `length` characters long."""
	# create empty variable for output
	out = ""
	# loop through range(length)
	for i in range(0, int(length)):
		# 1 in 4 chance for uppercase
		upper = random.randint(0, 3) is 3
		# check for uppercase
		# note: if uppercase, a different letter can be picked from the one that'd be used if not uppercase; this adds to the randomness and because of that will remain like this.
		if upper:
			out = out + chars[random.randint(0, len(chars)-1)].upper()
		else:
			out = out + chars[random.randint(0, len(chars)-1)].lower()
	# return output
	return out
	
def word(length):
	"""Uses a simple loop to create somewhat pronounce-able words. `length` is used for a base word, so the output is not guaranteed to be `length` characters long."""
	length 	= int(length)
	word 	= ""
	if length == 0 or length < 0:
		print("Length must be a positive number!")
		return ""
	random_a = random.randint(0, 1)
	if random_a == 0:
		word = consonants[random.randint(0, len(consonants) - 1)]
	else:
		word = vowels[random.randint(0, len(vowels) - 1)]
	for number in (range(length - 1)):
		if word[len(word) - 1] == 's':
			combination = bool(random.randint(0, 1))
			if combination:
				word = word + 'h'+ vowels[random.randint(0, len(vowels) - 1)]
			else:
				word = word + vowels[random.randint(0, len(vowels) - 1)]
		elif word[len(word) - 1] == 'c':
			combination = bool(random.randint(0, 1))
			if combination:
				word = word + 'h'+ vowels[random.randint(0, len(vowels) - 1)]
			else:
				word = word + vowels[random.randint(0, len(vowels) - 1)]
		elif word[len(word) - 1] == 't':
			combination = bool(random.randint(0, 1))
			if combination:
				word = word + 'ch'+ vowels[random.randint(0, len(vowels) - 1)]
			else:
				word = word + vowels[random.randint(0, len(vowels) - 1)]
		elif word[len(word) - 1] == 'o':
			double = bool(random.randint(0, 1))
			if not double:
				word = word + consonants[random.randint(0, len(vowels) - 1)]
			else:
				word = word + 'o' + consonants[random.randint(0, len(vowels) - 1)]
		elif word[len(word) - 1] == 'h':
			word = word + vowels[random.randint(0, len(vowels) - 1)]
		elif word[len(word) - 1] in consonants:
			word = word + vowels[random.randint(0, len(vowels) - 1)]
		elif word[len(word) - 1] in vowels:
			double = bool(random.randint(0, 1))
			consonant = consonants[random.randint(0, len(vowels) - 1)]
			if not double:
				word = word + consonant
			elif double and consonants is 'h':
				word = word + consonant
			else:
				word = word + consonant + consonant

	return word
	
def email(length, word=True):
	"""Uses `generate_code` or `generate_word` with `create_email` to generate fully randomized e-mails."""
	# if word, uses generate_word()
	# if not word, uses generate_code()
	if word:
		return create_email(generate_word(length))
	else:
		return create_email(generate_code(length))