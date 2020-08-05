#include<cmath>
using namespace std;

double distance2d(double from[2], double to[2])
{
	double diffX = abs(from[0] - to[0]);
	double diffY = abs(from[1] - to[1]);
	double delta = sqrt(pow(diffX, 2) + pow(diffY, 2));
	return delta;
}

double distance3d(double from[3], double to[3])
{
	double from2d[2] = {from[0], from[2]};
	double to2d[2] = {to[0], to[2]};
	double diffX = distance2d(from2d, to2d);
	double diffY = abs(from[1] - to[1]);
	double delta = sqrt(pow(diffX, 2) + pow(diffY, 2));
	return delta;
}