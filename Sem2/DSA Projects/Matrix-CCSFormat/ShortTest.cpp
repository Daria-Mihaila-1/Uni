#include <assert.h>
#include "Matrix.h"
#include <iostream>
using namespace std;
void  testAll() { 
	Matrix m(4, 4);
	assert(m.nrLines() == 4);
	assert(m.nrColumns() == 4);	
	m.modify(1, 1, 5);
	assert(m.element(1, 1) == 5);
	m.modify(1, 1, 6);
	assert(m.element(1, 2) == NULL_TELEM);
	
	//Teste ResizeMat
	m.ResizeMat(5,5);
	assert(m.nrLines() == 5);
	assert(m.nrColumns() == 5);	
	m.ResizeMat(3,3);
	assert(m.nrLines() == 3);
	assert(m.nrColumns() == 3);	
	m.modify(2, 2, 10);
	assert(m.element(2, 2) == 10);
	for (int i = 0; i< 10; i++)
	{
		m.ResizeMat(i,i+1);
	}	
	assert(m.nrLines() == 9);
	assert(m.nrColumns() == 10);
	
	for (int i = 100; i> 0; i--)
	{
		m.ResizeMat(i,i+1);
	}
	assert(m.nrLines() == 1);
	assert(m.nrColumns() == 2);
	
	cout << "am terminat" << endl;
}

int  main()
{
	testAll();
	return 0;
}