def distance2d(from, to)
	diff_x = (from[0] - to[0]).abs
	diff_y = (from[1] - to[1]).abs
	delta = Math.sqrt((diff_x ** 2) + (diff_y ** 2))
	return delta
end

def distance3d(from, to)
	from2d = [from[0], from[2]]
	to2d = [to[0], to[2]]
	diff_x = distance2d(from2d, to2d)
	diff_y = (from[1] - to[1]).abs
	delta = Math.sqrt((diff_x ** 2) + (diff_y ** 2))
	return delta
end

if __FILE__ == $0
	a = [1, 2, 3]
	b = [4, 5, 6]
	puts(distance3d(a, b))
end