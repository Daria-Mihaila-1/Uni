#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>
using namespace std;

//Komplexität : Teta(const)
SortedBag::SortedBag(Relation r) {
	//TODO - Implementation
	this->Nr_Elements = 0;
	this->relation = r;

	this->head = nullptr;
	this->tail = nullptr; 
	
	
}

//Komplexität : Teta(const)
void SortedBag::add_to_beginning(Node* new_node)
{
	new_node->next = head;
	new_node->prev = nullptr;
	head->prev = new_node;
	head = new_node;
}

//Komplexität : Teta(const)
void SortedBag::add_to_end(Node* new_node)
{
	new_node->prev = tail;
	new_node->next = nullptr;
	tail->next = new_node; 
	tail= new_node;
}


//Komplexität : O(Nr_Elements)
void SortedBag::add(TComp e) {
	//TODO - Implementation
	//#1 e <= alle El der Liste
	
	Node* new_node = new Node;
	new_node->info = e;
	if (Nr_Elements == 0)
	{
		
		this->head = new_node;
		this->tail = new_node;
		head->next = nullptr;
		head->prev = nullptr;
		tail->next = nullptr;
		tail->prev = nullptr;
		

	}
	else if (Nr_Elements == 1)
	{
		
		if (relation(e,head->info))
		{
			tail->prev = new_node;
			new_node->next = tail;
			head = new_node;
			new_node->prev = nullptr;
		}
		else
		{
			head->next = new_node;
			new_node->prev = tail;
			new_node->next = nullptr;
			tail = new_node;
			
		}
	} 
	else
	{	//1->2->10->20
		//e = 9
		Node* current = this->head;
		while (current != nullptr && not relation(e,current->info))  // relation : <    while e >= info do: 
		{
			current = current->next;
		}
		if (current == head)
		{
			add_to_beginning(new_node);
		}
		else if (current == nullptr)
		{
			add_to_end(new_node);

		}
		else  //add inside of the list
		{
			new_node->next = current;
			new_node->prev = current->prev;
			current->prev->next = new_node;
			current->prev = new_node;
		}
	}

	this->Nr_Elements++;
}

//Komplexität : Teta(const)
void SortedBag::remove_from_end(Node* current)
{
	if (Nr_Elements == 1)
	{
		this->head = nullptr;
		this->tail = nullptr;
		delete current;		
	}
	if (Nr_Elements == 2)
	{
		this->tail = head;
		
		this->tail->next = nullptr;
		this->tail->prev = nullptr;
		
		this->head->prev = nullptr;
		this->head->next = nullptr;
		
		delete current;
	}
	else
	{
		tail = tail->prev;
		tail->next = nullptr;
		delete current;
	}
	
}

//Komplexität : Teta(const)
void SortedBag::remove_from_beginning(Node* current)
{
	if (Nr_Elements == 1)
	{
		this->head = nullptr;
		this->tail = nullptr;
		delete current;
	}
	else if (Nr_Elements == 2)
	{
		this->head = tail;
		
		this->head->next = nullptr;
		this->head->prev = nullptr;
		
		this->tail->prev = nullptr;
		this->head->next = nullptr;
		delete current;
	}
	else
	{
		head = head->next;
		head->prev = nullptr;
		delete current;
	}
}


//Komplexität : Teta(const)
void SortedBag::remove_from_inside(Node* current)
{
	current->prev->next = current->next;
	current->next->prev = current->prev;
	delete current;
}


//Komplexität : O(Nr_Elements)

bool SortedBag::remove(TComp e) {
	
	if (nrOccurrences(e) == 0)
		return false;
	
	Node* current = this->head;
	//100% there is such an element in my list
	while (current->info != e)
	{
		current = current->next;
	}
	if (current == this->head)
		remove_from_beginning(current);

	else if (current == this->tail)
		remove_from_end(current);
	else
	{
		remove_from_inside(current);
	}
	Nr_Elements--;
	return true;

}

//Komplexität : O(Nr_Elements)
bool SortedBag::search(TComp elem) const {
	if (nrOccurrences(elem) != 0)
		return true;
	return false;
}

//Komplexität : O(Nr_Elements)
int SortedBag::nrOccurrences(TComp elem) const {
	//TODO - Implementation
	
	if( this->isEmpty() || not relation(elem, tail->info))
		return 0;

	Node* current = head;
	int count = 0;
	
	for (int i = 0; i< Nr_Elements; i++)
	{
		if (current->info == elem)
			break;
		current = current->next;
	}

	while (current != nullptr && current->info == elem)
	{	count++;
		current = current->next;
	}
	return count;
}


//Komplexität : Teta(const)
int SortedBag::size() const {
	
	return this->Nr_Elements;
}

//Komplexität : Teta(const)
bool SortedBag::isEmpty() const {

	if (this->Nr_Elements == 0)
		return true;
	return false;
}


//Bonus Function : delete n occurrences of a given element Elem
//Komplexität :  Worst Case : O(Nr_Elements)
// Best Case : Teta(1)  --> throws an exception at the beginning 
void SortedBag::delete_n(int n, TComp Elem)
{
	if (n > Nr_Elements || Nr_Elements == 0)
		throw exception();

	Node* current = this->head;
	while (current != nullptr && current->info != Elem)
	{
		current = current->next;
	} 
	
	if (current == nullptr)
	{
		cout <<"element not found" << endl;
		throw exception();
	}

	int count = n;
	if (current == head)
	{
			while (Nr_Elements != 0 && head->info == Elem && count > 0)
			{
				head = head->next;
				delete current;
				current = head;
				head->prev = nullptr;
				Nr_Elements--;
				count--;
			}
			if (count > 0)
				throw exception();
	}
	else if (current == tail)
	{
			if (n == 1)
			{
				tail = tail->prev;
				tail->next = nullptr;
				delete current;
				Nr_Elements--;
			}
			else 
				
				throw exception();
	}
	else 
	{
			Node* aux = current;
			while (current != nullptr && current->info == Elem && count > 0)
			{
				aux = current; //aux points to current
				current->prev->next = current->next;
				current->next->prev = current->prev; //making the links to remove the node to what current points to
				current = current->next; 
				delete aux; // deleting the node to what current pointed to 
				
				count--;
				Nr_Elements--;
				
			}
			if (count > 0)
				throw exception();
	}
	
}


SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}

//Komplexität : Teta(Nr_Elements)
SortedBag::~SortedBag() {
	//TODO - Implementation

	Node*current = this->head;

	for (int i = 0; i < Nr_Elements; i++)
	{	
		if (current->next == nullptr)
			break;
		else
			current= current->next;
		delete current->prev;
	}	
	delete current;
	
}
