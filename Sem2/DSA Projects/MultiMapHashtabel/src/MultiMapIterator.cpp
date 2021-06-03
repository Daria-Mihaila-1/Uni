#include "MultiMapIterator.h"
#include "MultiMap.h"


MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
	this->pos = 0;
	while(this->pos < this->col.m && this->col.Elements[pos] == nullptr)
	{
		pos++;
	}
	if (this->pos < this->col.m)
		
		this->currentNode = this->col.Elements[pos];
	else
		this->currentNode = nullptr;
}

TElem MultiMapIterator::getCurrent() const{
	if (!valid())
		throw exception();
	return this->currentNode->elem;
}

bool MultiMapIterator::valid() const {
	if (this->currentNode != nullptr && this->pos < this->col.m)
		return true;
	return false;
}

void MultiMapIterator::next() {
	
	if (!this->valid())
		throw exception();
	if (this->currentNode->next != nullptr)
	{
		this->currentNode = this->currentNode->next;
	}
	else
	{
		this->pos++;
		while (this->pos < this->col.m && this->col.Elements[pos] == nullptr)
		{
			this->pos++;
		}
		if (this->pos < this->col.m)
		
			this->currentNode = this->col.Elements[pos];
		else
			this->currentNode = nullptr;
	}
}

void MultiMapIterator::first() {
	this->pos = 0;
	while(this->pos < this->col.m && this->col.Elements[pos] == nullptr)
	{
		pos++;
	}
	if (this->pos < this->col.m)
		
		this->currentNode = this->col.Elements[pos];
	else
		this->currentNode = nullptr;
}

