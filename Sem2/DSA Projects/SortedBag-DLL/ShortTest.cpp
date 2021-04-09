#include "ShortTest.h"
#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <assert.h>
#include <iostream>
using namespace std;

bool relation1(TComp e1, TComp e2) {
	return e1 <= e2;
}

void testAll() {
	SortedBag sb(relation1);
	sb.add(5);
	sb.add(6);
	sb.add(0);
	sb.add(5);
	sb.add(10);
	sb.add(8);
	
	assert(sb.size() == 6);
	assert(sb.nrOccurrences(5) == 2);

	assert(sb.remove(5) == true);
	assert(sb.remove(9) == false);
	assert(sb.size() == 5);
	assert(sb.search(6) == true);
	assert(sb.isEmpty() == false);
	
	SortedBagIterator it = sb.iterator();
	
	assert(it.valid() == true);
	
	while (it.valid()) {
		it.getCurrent();
		it.next();
	}
	
	assert(it.valid() == false);
	it.first();
	assert(it.valid() == true);
	sb.add(5);
	sb.add(5);
	sb.add(5);
	sb.add(5);

	sb.delete_n(5,5);
	assert(sb.nrOccurrences(5) == 0);
	
	try
	{
		sb.delete_n(2, 10);
	}
	catch(...)
	{
		sb.delete_n(1, 10);
	}
	assert(sb.nrOccurrences(10) == 0);
	
	try 
	{
		sb.delete_n(10,0);
	}
	catch(...)
	{
		sb.delete_n(1, 0);
	}
	assert(sb.nrOccurrences(0) == 0);
	
	sb.add(3);
	sb.add(3);
	sb.add(3);
	sb.delete_n(2,3);
	
	assert(sb.nrOccurrences(3) == 1);
}
