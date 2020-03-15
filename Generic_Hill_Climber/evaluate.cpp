
/*
 filename: evaluate.cpp
 author: Sara Davis 
 date: 9/7/2019
 version: 1.0
 description: c++ implementation of a hillclimber

*/

#include <iostream>
using namespace std;


double eval (int *vec)
{
	double ttl = 0.0;

	if (vec[50] == 1){
		for (int i = 0; i < 100; i++){
			if (vec[i] == 1 && i != 50)
			{
				return 0.0;
			}
		}
		return 100.00;
	}
	else
		return 0.0;

}