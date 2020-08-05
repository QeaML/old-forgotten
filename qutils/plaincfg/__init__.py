"""PlainCFG Formatter

Example usage:

	>>> import qutils.plaincfg
	>>> qutils.plaincfg.to_dict(\"\"\"name John Doe
	age 24\"\"\")
	{'name': 'John Doe', 'age': '24'}
	>>> qutils.plaincfg.from_dict({'name':'John Doe','age':'24'})
	name John Doe
	age 24
	
"""

__name__ 	= "plaincfg"
__author__ 	= "QeaML <qeaml@wp.pl>"

def to_dict(cfg):
	out = {}
	cfg = str(cfg)
	for setting in cfg.split('\n'):
		name 	= setting.split(' ')[0]
		value	= ' '.join(setting.split(' ')[1:])
		out.update({name: value})
	return out
	
def from_dict(src):
	out = []
	if src.__class__ == dict:
		for key in src:
			out.append(str(key)+' '+str(src[key]))
		return '\n'.join(out)
	else:
		raise TypeError('src must be a dict')