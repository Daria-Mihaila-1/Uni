#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	
	this->current = bag.head;

}

//Komplexitat : Teta(1)
TComp SortedBagIterator::getCurrent() {
	//TODO - Implementation
	if (this->current == nullptr || bag.size() == 0 || bag.isEmpty())
		throw exception();

	return this->current->info;
}

//Komplexitat : Teta(1)
bool SortedBagIterator::valid() {
	//TODO - Implementation
	if (this->current != nullptr)
		return true;
	return false;
}

//Komplexitat : Teta(1)
void SortedBagIterator::next() {
	//TODO - Implementation
	if (this->current == nullptr)
		throw exception();

	this->current = this->current->next;
}

//Komplexitat : Teta(1)
void SortedBagIterator::prev()
{
	if (this->current == nullptr || bag.size() == 0)
		throw exception();
	this->current = current->prev;
}

//Komplexitat : Teta(1)
void SortedBagIterator::first() {
	//TODO - Implementation
	this->current = bag.head;
}

