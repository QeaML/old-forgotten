function distance2d(from, to){
	diffX = Math.abs(from[0] - to[0]);
	diffY = Math.abs(from[1] - to[1]);
	delta = Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
	return delta;
};

function distance3d(from, to){
	from2d = [from[0], from[2]];
	to2d = [to[0], to[2]];
	diffX = distance2d(from2d, to2d);
	diffY = Math.abs(from[1] - to[1]);
	delta = Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
	return delta;
};

a = [1, 2, 3];
b = [4, 5, 6];
console.log(distance3d(a, b));