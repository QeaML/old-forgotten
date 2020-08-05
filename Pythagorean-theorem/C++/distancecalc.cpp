#include<iostream>
#include"distancecalc.h"
using namespace std;

int main()
{
	double a[3] = {1.0, 2.0, 3.0};
	double b[3] = {4.0, 5.0, 6.0};
	double distance = distance3d(a, b);
	cout << distance << endl;
	if(distance > 5.0)
	{
		return 0;
	} else {
		return 1;
	}
}