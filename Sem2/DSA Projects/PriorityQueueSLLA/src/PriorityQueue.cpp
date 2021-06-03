#include <iostream>
#include "PriorityQueue.h"
#include <exception>
#include <stack>
//inclus pt functia suplimentara

using namespace std;
//elements with the highest priority get removed first 

PriorityQueue::PriorityQueue(Relation r) {
	this->rel = r;
	this->cap = 7; 
	this->size = 0;
	this->head = -1;
	this->tail = -1;
	this->HighestPriority = -1;
	this->firstEmpty = 0;

	this->Values = new Node[cap];
	
	for (int i = 0 ; i < cap-1; i++) {
		Values[i].next = i+1;
	}
	this->Values[cap-1].next = -1; 
}


void PriorityQueue::push(TElem e, TPriority p) {
	
	if (this->size == 0) {
		this->size++;
		this->head = this->firstEmpty;
		this->tail = this->head;

		this->Values[head].info.first = e;
		this->Values[head].info.second = p;
		this->firstEmpty = this->Values[firstEmpty].next;
		this->Values[tail].next = -1;
	
		this->HighestPriority = head;
	}
	
	else if (this->size == 1) {
		
		this->size++;

		this->Values[firstEmpty].info.first = e;
		this->Values[firstEmpty].info.second = p;
		//setam valoarea lui Values[firstEmpty]
		
		this->tail = firstEmpty;
		//setam tail ul pe elementul "creat"

		this->Values[head].next = tail;
		
		firstEmpty = Values[firstEmpty].next;  //firstEmpty merge mai departe 
		
		this->Values[tail].next = -1;//nextul lui tail va fi nullptr

		if (rel(Values[head].info.second, p))
			this->HighestPriority = head;
		else 
			this->HighestPriority = tail;
	
	} else {
		// !!! introducem doar la capatul queue ului
		this->size++;
		if (this->firstEmpty == -1)
		{
			resize('g');
		}

		Values[firstEmpty].info.first = e;
		Values[firstEmpty].info.second = p;

		Values[tail].next = firstEmpty;
		this->tail = firstEmpty;
		
		firstEmpty = Values[firstEmpty].next;
		
		Values[this->tail].next = -1;
		
		if (!rel(Values[HighestPriority].info.second, p))
			this->HighestPriority = tail;
	}	

}

Element PriorityQueue::top() const {
	//throws exception if the queue is empty
	
	if (this->isEmpty())
		throw exception();
	
	return Values[HighestPriority].info;
}

Element PriorityQueue::pop() {
	
	if (this->size == 0)
		throw exception();
	
	Element value;
	
	value = Values[HighestPriority].info;        //valoarea de retur
	
	if (this->size == 1) {

		this->head = -1;
		this->tail = -1;

		Values[HighestPriority].next = firstEmpty;
		firstEmpty = HighestPriority;
					
		//am un singur element care e pe indexul head si tail si leg array ul de firstEmpty de pozitia lui

		this->HighestPriority = -1;

	} 
	else if (this->size == 2) { 
		
		
		
		if (HighestPriority == head) {
			
			Values[HighestPriority].next = firstEmpty;
			firstEmpty = HighestPriority;

			Values[HighestPriority].info.first = 0;
			head = tail;

			HighestPriority = head;

		} else {
			
			Values[HighestPriority].next = firstEmpty;
			firstEmpty = HighestPriority;

			Values[HighestPriority].info.first = 0;
			
			tail = head;
			Values[tail].next = -1;

			HighestPriority = tail;
		}

	} else {

		if (HighestPriority == head)
			{Values[HighestPriority].info.first = 0;
			head = Values[head].next;}
           //if the element with highestPriority is first in priority queue then simply move head on head.next
	
		else 
		{		//daca nu cautam parcurgem cu un index "pointer" current queue ul 
		 		//pana cand Values[current].next == HighestPriority
			int current = head;

			while (Values[current].next != HighestPriority) {
				current = Values[current].next;	
			}
			
			if (HighestPriority == tail)
			{
				this->tail = current;  
				Values[this->tail].next = -1;
			}
			else
				Values[current].next = Values[Values[current].next].next;
			
		
		}

		Values[HighestPriority].next = firstEmpty;
		firstEmpty = HighestPriority;
		
		HighestPriority = searchHighest();
	}
	
	this->size--;	

	return value;
}

//Komplexitat : O(n)
bool PriorityQueue::isEmpty() const {
	if (this->size == 0)
		return true;
	return false;
}

//Komplexitat : Theta(n)
void PriorityQueue::resize(char message)
{
	Node* Array;

	//firstly setting the firstEmpty index on the first memory space after the last element of the priority queue
	//then doubling the capacity  
	this->firstEmpty = cap;
	this->cap = this->cap * 2;
	
	Array = new Node[cap]; //new array of doubled capacity

	for (int i = 0; i < size; i++)
	{ 
		Array[i] = Values[i];
	}
	//as in the constructor initialising our virtual empty slots array 
	for (int i = cap/2; i < cap - 1; i++) {
		Array[i].next = i+1;
	}
	Array[cap-1].next = -1;
	
	this->Values = Array;
}

//for when the element with the highest priority is removed 
//searching for a new one
//Komplexitat : O(n)
//Best case : Theta(1)
//Worst case : Theta(n)
int PriorityQueue::searchHighest()
{
	
	int current = head;
	int highest = current;
	while (current != -1) {
		if (rel(Values[current].info.second, Values[highest].info.second)) {
			highest = current;
		}
		current = Values[current].next;
	}
	return highest;
}

//Elements are printed with the help of the pop() function
//Komplexitat : Theta(n)   
void PriorityQueue::PrintQueue()
{
	int sizecopy = size;
	stack<Element> Values_aux;
	int i;
	for(; i < sizecopy; i++)
	{
		//we call pop() and push the returned element onto a stack so that we don't lose the value
		Values_aux.push(this->pop());

		//then we can print the recently onto the stack pushed element
		cout << Values_aux.top().first << ' ';
	}
	
	//afterwards we push all elements from the stack back into the  priority queue
	for (i = 0; i < sizecopy; i++)
	{
		this->push(Values_aux.top().first, Values_aux.top().second);
		Values_aux.pop();
	}
}


PriorityQueue::~PriorityQueue() {
	
	delete[] this->Values;
};
