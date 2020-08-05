"""PlainCFG 2.0 Formatter

Example usage:
	
	>>> import qutils.plaincfg2
	>>> qutils.plaincfg2.format(\"\"\"name:str John Doe
	age:int 24\"\"\")
	{'name':'John Doe', 'age':24}
	>>> qutils.plaincfg2.create({'name':'John Doe', 'age':24})
	name:str John Doe
	age:int 24
	
"""

__name__ 	= "plaincfg2"
__author__ 	= "QeaML <qeaml@wp.pl>"

def to_dict(cfg):
	out = {}
	cfg = str(cfg)
	for setting in cfg.split('\n'):
		if ":" in setting.split(' ')[0]:
			name 	= setting.split(" ")[0].split(":")[0]
			type 	= setting.split(" ")[0].split(":")[1]
			value	= " ".join(setting.split(" ")[1:])
			if type == 'int':
				value = int(value)
			elif type == 'flt':
				value = float(value)
			elif type == 'str':
				value = str(value)
			elif type.startswith('arr'):
				subtype = type.split('/')[1]
				strvalues = str(value).split(",")
				finalvalues = []
				for string in strvalues:
					if subtype == 'int':
						finalvalues.append(int(string))
					elif subtype == 'flt':
						finalvalues.append(float(string))
					elif subtype == 'str':
						finalvalues.append(str(string))
					else:
						finalvalues.append(string)
				value = finalvalues
			else:
				value = str(value)
		else:
			name	= setting.split(" ")[0]
			value	= " ".join(setting.split(" ")[1:])
		out.update({name: value})
	return out
	
def from_dict(src):
	out = []
	if src.__class__== dict:
		for key in src:
			line	 = str(key)+":"
			keytype	 = src[key].__class__
			if keytype == str:
				line = line+"str"+" "+str(src[key])
			elif keytype == int:
				line = line+"int"+" "+str(src[key])
			elif keytype == float:
				line = line+"flt"+" "+str(src[key])
			elif keytype == list:
				line = line+"arr/str"+" "
				items = []
				for item in src[key]:
					items.append(str(item))
				line = line+",".join(items)
			else:
				line = line+"str"+" "+str(src[key])
			out.append(line)
		return '\n'.join(out)
	else:
		raise TypeError('src must be a dict')