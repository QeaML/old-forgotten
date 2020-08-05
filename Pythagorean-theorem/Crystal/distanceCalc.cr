def distance2d(from : Array(Float), to : Array(Float))
	diffX = (from[0] - to[0]).abs
	diffY = (from[1] - to[1]).abs
	delta = Math.sqrt((diffX ** 2) + (diffY ** 2))
	delta
end

def distance3d(from : Array(Float), to : Array(Float))
	from2d = [from[0], from[2]]
	to2d = [to[0], to[2]]
	diffX = distance2d(from2d, to2d)
	diffY = (from[1] - to[1]).abs
	delta = Math.sqrt((diffX ** 2) + (diffY ** 2))
	delta
end

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
puts distance3d(a, b)