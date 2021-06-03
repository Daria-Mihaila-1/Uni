#pragma once
#include "SortedSet.h"
#include <stack>
#include <iostream>

//DO NOT CHANGE THIS PART


class SortedSetIterator
{
	friend class SortedSet;
	
private:
	const SortedSet& multime;
	SortedSetIterator(const SortedSet& m);

	std::stack<Node*> stack; 
	Node* currentNode; 

	
public:
	void first();
	void next();
	TElem getCurrent();
	bool valid() const;
};

