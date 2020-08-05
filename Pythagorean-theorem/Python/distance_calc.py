from math import sqrt

def distance2d(_from, to):
	diffX = abs(_from[0] - to[0])
	diffY = abs(_from[1] - to[1])
	delta = sqrt((diffX ** 2) + (diffY ** 2))
	return delta
	
def distance3d(_from, to):
	from2d = (_from[0], _from[2])
	to2d = (to[0], to[2])
	diffX = distance2d(from2d, to2d)
	diffY = abs(_from[1] - to[1])
	delta = sqrt((diffX ** 2) + (diffY ** 2))
	return delta
	
if __name__ == "__main__":
	a = (1, 2, 3)
	b = (4, 5, 6)
	distance = distance3d(a, b)
	print(distance)
	if distance > 5.0:
		exit(0)
	else:
		exit(1)