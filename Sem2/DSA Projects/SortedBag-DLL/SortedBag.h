#pragma once
//DO NOT INCLUDE SORTEDBAGITERATOR

//DO NOT CHANGE THIS PART
typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);
#define NULL_TCOMP -11111;

class SortedBagIterator;
struct Node
{
	TComp info;
	struct Node *next;  //pointer the next node
	struct Node *prev;  //pointer to the previous node 
};

class SortedBag {
	friend class SortedBagIterator;

private:
	int Nr_Elements;  //saves the nr of nodes the DLL has
	Node* head;  //a pointer to the first node of the DLL
	Node* tail;  //a pointer to the first node of the DLL
	Relation relation;	//the relation by which the bag is sorted

	//removes a given node from the beginning of the DLL deleting it from the memory as well
	void remove_from_end(Node* pointer);
	
	//removes a given node from the beginning of the DLL deleting it from the memory as well
	void remove_from_beginning(Node* current);
	
	//removes a given node from the inside of the DLL deleting it from the memory as well
	void remove_from_inside(Node* current);

	//adds new_node to the beginning of the DLL
	void add_to_beginning(Node* new_node);
	
	//adds new_node to the end of the DLL
	void add_to_end(Node* new_node);


public:
	//constructor
	SortedBag(Relation r);

	//adds an element to the sorted bag
	void add(TComp e);

	//removes one occurence of an element from a sorted bag
	//returns true if an element was removed, false otherwise (if e was not part of the sorted bag)
	bool remove(TComp e);

	//checks if an element appearch is the sorted bag
	bool search(TComp e) const;

	//returns the number of occurrences for an element in the sorted bag
	int nrOccurrences(TComp e) const;

	//returns the number of elements from the sorted bag
	int size() const;

	//returns an iterator for this sorted bag
	SortedBagIterator iterator() const;

	//checks if the sorted bag is empty
	bool isEmpty() const;

	void delete_n(int n, TComp elem);

	//destructor
	~SortedBag();
};