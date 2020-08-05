# qutils.creators

import random

def email(username):
	"""Create a randomized e-mail based on the supplied username."""
	# variables for emails
	domains = ["gmail.com", "mailo.com", "aol.com", "hotmail.com", "outlook.com"]
	spaces 	= "_-."
	illegal = ["#", "'", '"', "@", ":", ";", "/", "?", "!", "$", "%", "^", "&", "*", "(", ")", "=", "+", "|", ",", "{", "}", "[", "]", "`", "~", "<", ">", "€", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	# remove illegal characters from email
	for char in spaces:
		if char in username:
			username = username.replace(char, " ")
	for char in illegal:
		if char in username:
			username = username.replace(char, "")
	# replace spaces in username (if any) with either "_", "-" or "."
	a = username.lower().replace(" ", spaces[random.randint(0, len(spaces) - 1)])
	# choose a random domain
	b = domains[random.randint(0, len(domains) - 1)]
	# choose number type
	c = random.randint(0, 1)
	if c == 0:
		# year-like number
		d = random.randint(1995, 2019)
	else:
		# normal number
		d = random.randint(1, 99)
	# put it together
	e = f"{a}{d}@{b}"
	# return final email
	return e