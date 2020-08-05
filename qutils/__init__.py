"""QeaML's common utility functions and variables."""
# qutils.__init__

__name__ = "qutils"
__author__ = "QeaML <qeaml@wp.pl>"

import datetime

# common variables
alphabet 	= "abcdefghijklmnopqrstuwvxyz"
numbers 	= "1234567890"
chars 		= "abcdefghijklmnopqrstuwvxyz1234567890"
consonants 	= "bcdfghjklmnpqrstwvxyz"
vowels 		= "aeiou"

class logger:
	"""A pretty simple logger, allowing to write to console and a file at the same time.

Example usage:

	from qutils import logger
	log = logger()
	log.log('Hello world!')"""
	
	def __init__(this, write_console=True, write_file=True, datetime_source=datetime.datetime):
		"""Creates a `logger` instance.

		Parameters:
			write_console (boolean): if True, the logger will write to the print() function
			write_file (boolean): if True, the logger will write to a file (name based on current time from datetime_source)
			datetime_source: a source of dates and time (must implement now())
		"""
		this.write_console = bool(write_console)
		this.write_file = bool(write_file)
		if this.write_console == False and this.write_file == False:
			raise NameError('__init__ needs either write_console or write_file to be True')
		this.datetime = datetime_source
		if not 'now' in dir(this.datetime):
			raise NameError('datetime_source value must implement now() function')
		if this.write_file:
			this.file = str(this.datetime.now()).replace(':', ' ')+'.log'
			open(this.file, 'xt').write(' --- START OF LOG --- ')
			this.log('Logger initialised. Logging to file '+this.file)
		else:
			this.log('Logger initialised.')
		
	def log(this, msg, level=0):
		"""Create a log entry
		
		Parameters:
			msg (string): the entry's message
			level (int): the entry's level
				0 and below = INFO
				1 = WARN
				2 = ERR
				3 and above = CRITICAL
		"""
		msg = str(msg)
		if level == 0:
			level = 'INFO'
		elif level == 1:
			level = 'WARN'
		elif level == 2:
			level = 'ERR'
		elif level == 3:
			level = 'CRITICAL'
		elif level < 0:
			level = 'INFO'
		elif level > 3:
			level = 'CRITICAL'
		msg = '['+str(this.datetime.now())+'] ['+level+'] '+msg
		if this.write_console:
			print(msg)
		if this.write_file:
			open(this.file, 'at').write(msg+'\n')
			
	def end(this):
		"""Ends the log, disabling all logging methods."""
		this.log('Log ended.')
		open(this.file, 'xt').write(' --- END OF LOG --- ')
		this.write_file = False
		this.write_console = False