#include<math.h>
#include<stdlib.h>

/*
**	distancecalc.h for C
**	QeaML, 07.02.2020
*/

double distance2d(double from[2], double to[2])
{
	double diffx;
	double diffy;
	double delta;
	
	diffx = abs(from[0] - to[0]);
	diffy = abs(from[1] - to[1]);
	delta = sqrt(pow(diffx, 2.0) + pow(diffy, 2.0));
	return delta;
}

double distance3d(double from[3], double to[3])
{
	double diffx;
	double diffy;
	double delta;
	
	double from2d[2] = {from[0], from[2]};
	double to2d[2] = {to[0], to[2]};
	diffx = distance2d(from2d, to2d);
	diffy = abs(from[1] - to[1]);
	delta = sqrt(pow(diffx, 2.0) + pow(diffy, 2.0));
	return delta;
}