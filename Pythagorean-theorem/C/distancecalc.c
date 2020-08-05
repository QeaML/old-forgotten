#include<stdio.h>
#include"distancecalc.h"

/*
**	distancecalc.c for C
**	QeaML, 07.02.2020
*/

int main()
{
	double distance;
	
	double a[3] = {1.0, 2.0, 3.0};
	double b[3] = {4.0, 5.0, 6.0};
	distance = distance3d(a, b);
	
	printf("%lf", distance);
	
	if(distance > 5.0)
	{
		return 0;
	} else {
		return 1;
	}
}