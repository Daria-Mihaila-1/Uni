#include "ShortTest.h"
#include "ExtendedTest.h"
#include "SortedSet.h"
#include "SortedSetIterator.h"
#include <iostream>

using namespace std;

bool r3(TComp e1, TComp e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	testAll();
	testAllExtended();
	SortedSet s1(r3);
	assert(s1.add(5) == true);
	assert(s1.add(1) == true);
	assert(s1.add(10) == true);
	assert(s1.add(2) == true);
	SortedSet s10(r3);
	/*s10 = s1.add_from_interval(2, 5);
	assert(s10.search(5) == true);
	assert(s10.search(10) == false);
	assert(s10.search(2) == true);
	*/cout << "Test end" << endl;
	system("pause");
}