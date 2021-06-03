#pragma once
//DO NOT INCLUDE SETITERATOR
#include <stack>

//DO NOT CHANGE THIS PART
typedef int TElem;
typedef TElem TComp;
typedef bool(*Relation)(TComp, TComp);
#define NULL_TELEM -11111
class SortedSetIterator;

struct Node
{
	Node* left;
	Node* right;
	TComp info;
};

Node* insert_rec(Node* node, TComp elem, Relation rel);
Node* remove_rec(Node* node, TComp elem, Relation rel);
Node* minimum(Node* node);

class SortedSet {
	friend class SortedSetIterator;
private:
	Relation rel;
	Node* root;
	int nrElem;

public:
	//constructor
	SortedSet(Relation r);

	//adds an element to the sorted set
	//if the element was added, the operation returns true, otherwise (if the element was already in the set) 
	//it returns false
	bool add(TComp e);
	
	SortedSet add_from_interval(int a, int b);

	//SortedSet add_from_interval_rec(int a, int b, Node* node);
	
	//removes an element from the sorted set
	//if the element was removed, it returns true, otherwise false
	bool remove(TComp e);

	//checks if an element is in the sorted set
	bool search(TElem elem) const;


	//returns the number of elements from the sorted set
	int size() const;

	//checks if the sorted set is empty
	bool isEmpty() const;

	//returns an iterator for the sorted set
	SortedSetIterator iterator() const;

	// destructor
	~SortedSet();


};
