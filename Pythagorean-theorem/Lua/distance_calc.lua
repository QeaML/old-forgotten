function distance2d(from, to)
    diffX = math.abs(from[1] - to[1])
    diffY = math.abs(from[2] - to[2])
    delta = math.sqrt((diffX ^ 2) + (diffY ^ 2))
    return delta
end

function distance3d(from, to)
    from2d = {from[1], from[3]}
    to2d = {to[1], to[3]}
    diffX = distance2d(from2d, to2d)
    diffY = math.abs(from[2] - to[2])
    delta = math.sqrt((diffX ^ 2) + (diffY ^ 2))
    return delta
end

a = {1.0, 2.0, 3.0}
b = {4.0, 5.0, 6.0}
print(distance3d(a, b))
