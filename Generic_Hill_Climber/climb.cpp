
/*
 filename: Generic_Hill_Climber.cpp
 author: Sara Davis 
 date: 9/7/2019
 version: 1.0
 description: c++ creation of a generic hillclimber
 note: Generates a generic array that would be searchable using a hillclimber
*/


#include <iostream>

using namespace std;
double eval(int *pj);

int main()
{
	int vec[100];
	for(int i = 0; i < 100; i++)
	{
		if (i == 50)
		{
			vec[i] = 1
		}
		else{
			vec[i] = 0;
		}
		
	}
	double val = eval(vec);
	cout << val << endl;
}