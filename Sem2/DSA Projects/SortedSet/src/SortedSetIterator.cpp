#include "SortedSetIterator.h"
#include <exception>
#include <vector>
using namespace std;

/*
Komplexität : 
Best case : Theta(1)
Worst case : O(n/2)  the root has only a left complete subtree 
*/
SortedSetIterator::SortedSetIterator(const SortedSet& m) : multime(m)
{
	this->currentNode = this->multime.root;
	
	//pushes the whole left subtree in the stack
	while (currentNode != nullptr)
	{
		this->stack.push(currentNode);
		currentNode = currentNode->left;
	}
	//if there is a left subtree then the currentNode will be placed on the last pushed node
	//if not currentNode just exists
	if (this->stack.empty())
		this->currentNode = nullptr;

	else 
		this->currentNode = this->stack.top();

}

/*
Komplexität : 
Best case : Theta(1)
Worst case : O(n/2)  the root has only a left complete subtree 
*/
void SortedSetIterator::first() {
	//does the same thing as the constructor, sets the currentNode on the most left node of the tree which should be the minimum
	std::stack<Node*> new_stack;
	this->stack = new_stack;
	Node* node = this->multime.root;
	while (node != nullptr)
	{
		this->stack.push(node);
		node = node->left;
	}
	if (this->stack.empty())
		this->currentNode = nullptr;

	else 
		this->currentNode = this->stack.top();
}

/*
Komplexität : 
Best case : Theta(1)
Worst case : O(n/2)  the root has only a left complete subtree 
*/
void SortedSetIterator::next() {
	if (!this->valid())
		throw exception();
	//takes a node out of the stack	
	Node* node = stack.top();	
	this->stack.pop();

	//in case it is a parent it goes to the right child
	if (node->right != nullptr)
	{	
		node = node->right;

		//then pushes the whole left subtree of the right child onto the stack if possible
		while(node != nullptr)
		{
			this->stack.push(node);
			node = node->left;
		}
	}

	//sets the currentNode on the most left node of that subtree
	//if possible
	if (this->stack.empty())
		this->currentNode = nullptr;

	else
		this->currentNode = this->stack.top();
}

//throws exception if iterator not situated on a valid position
//returns the current info if not
//Komplexität : Theta(1)
TElem SortedSetIterator::getCurrent()
{
	if (!valid())
		throw exception();
	else
		return currentNode->info;
		
}

//throws exception if iterator found "out of tree"
//Komplexität : Theta(1)
bool SortedSetIterator::valid() const {
	if (this->currentNode == nullptr || this->stack.empty())
		return false;
	return true;
}

