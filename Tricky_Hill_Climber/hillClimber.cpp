
/*
 filename: hillClimber.cpp
 author: Sara Davis 
 date: 9/13/2019
 version: 1.0
 description: c++ creation of a more complex hill climber

*/


#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include<algorithm>

using namespace std;

double eval(int *pj);
int * InitSolution();
int * mod(int * vec, vector<int> used, int j);


int main()
{

  int * sBest;
  int * sNew;
  int * sCur;
  int fBest = 0;
  int fNew;
  int fCur = 0;
  vector<int> used;

  srand (time(0));
  int i = 0;
  for (int i = 0; i < 1500000; i++)
  {
  	sCur = InitSolution();
  	fCur = eval(sCur);
  	cout << fCur << endl;
  	if (fCur >= fBest){
  		sBest = sCur;
  		fBest = fCur;
  	}
  	i++;
  }
  cout << fBest <<endl;
  for (int k = 0; k < 150; k++)
  {
  	cout << sBest[k] << " ";
  }
  cout << endl;

  int j=0;
  for (int i = 0; i < 100000000; i++)
  {
  	sNew = mod(sBest, used, j);
  	fNew = eval(sNew);
  
  	cout << "best " << fBest << " current " << fNew << endl;

  	if (fNew >= fBest)
  	{
  		sBest = sNew;
  		fBest = fNew;
  	}
  	if( j < 150)
  	{
  		j++;
  	}
  	if (j == 150)
  	{
  		j =0;
  	}


  }
  cout << "Fitness: " << fBest << endl;

  cout << "Vector contents: " << endl;

  for (int k = 0; k < 150; k++)
  {
  	cout << sBest[k] << " ";
  }
  cout << endl;



}


int * InitSolution()
{
	static int temp[150];

	for (int i = 0; i < 150; i++)
	{
		int num = rand() % 2;
		temp[i] = num;
	} 

	


	return temp;
}
//may need to modify to change 1 as well

int * mod(int * vec, vector<int> used, int j)
{
	if (vec[j] == 1)
	{
		vec[j] = 0;
	}
	else{
		vec[j] =1;
	}
	

	return vec;
}

