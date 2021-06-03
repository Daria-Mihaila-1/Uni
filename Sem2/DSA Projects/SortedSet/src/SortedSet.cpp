#include "SortedSet.h"
#include "SortedSetIterator.h"



//Komplexität : Theta(1)
SortedSet::SortedSet(Relation r) {
	this->rel = r;
	this->nrElem = 0;
	this->root = nullptr;			
}

//Komplxexität : O(nrOfLevels)
Node* insert_rec(Node* node, TComp elem, Relation rel)
{
	//if arrived to a nullptr creates a new node
	if (node == nullptr)
	{
		node = new Node;
		node->info = elem;
		node->right = nullptr;
		node->left = nullptr;
	}
	//if searched elem should be o the right side of the tree with root "node" search on the subtree that has the right child of "node" as a parent
	else if (rel(node->info, elem))
	{
		node->right = insert_rec(node->right, elem, rel);
	}

	//if searched elem should be o the left side of the tree with root "node" search on the subtree that has the left child of "node" as a parent
	else
	{
		node->left = insert_rec(node->left, elem, rel);
	}
	return node;
}
//Komplexitat : O(nrOfLevels)
/* DOESN'T WORK
SortedSet SortedSet::add_from_interval(int a, int b)
{
	if (minimum(this->root)->info > b)
		throw std::exception();
	SortedSet newset(rel);
	int nrElem2 = 0;
	Node* root2 = nullptr;
	Node* currentNode = this->root;
	while (currentNode != nullptr)
	{
		if (currentNode->info <= b && currentNode->info >= a)
		{
			root2 = insert_rec(root2, currentNode->info, rel);
			nrElem2++;
		}
		if (currentNode->right  != nullptr)
		{
			currentNode = currentNode->right;
		}
		else if (currentNode->left  != nullptr)
		{
			currentNode = currentNode->left;
		}		
	}
	newset.root = root2;
	newset.nrElem = nrElem2;
	
	return newset;
}
*/
bool SortedSet::add(TComp elem) {
	//if already in tree returns false
	if (search(elem))
		return false;

	this->root = insert_rec(this->root, elem, this->rel);
	this->nrElem++;

	return true;
}


//Komplexität : O(nrOfLevels)
bool SortedSet::remove(TComp elem) {
	//if elem not in tree don't even bother
	if (!search(elem))
		return false;
	
	this->root = remove_rec(this->root,elem, this->rel);
	this->nrElem--;
	
	return true;
}

//Komplexität : O(nrOfLevels)
Node* remove_rec(Node* node, TComp elem, Relation rel)
{
	//in search for the elem Node
	if (node == nullptr) 
	//I  have an empty tree :/
		return nullptr;

	else if ( node->info == elem)
	{
		//found my node!!
		
		//my Node has no children
		if (node->left == nullptr && node->right == nullptr)
		{
			delete node;
			return nullptr;
		}
		
		//my Node has 1 child( left || right)
		else if (node->left == nullptr)
			return node->right;
		
		else if (node->right == nullptr)
			return node->left;
		
		//my Node has 2 children
		//find the smallest value from the "right tree's" children and replace my Node with that 
		else
		{
			Node* min = minimum(node->right);
			node->info = min->info;
			//do that remove_rec for the right subtree of the found node too
			node->right = remove_rec(node->right, min->info, rel);
			return node;
		}
	}	
	//elem should be on the right side of the tree with parent "node"--->go search there 
	else if (rel(node->info, elem))
	{
		node->right = remove_rec(node->right, elem, rel);
		return node;
	}

	//elem should be on the right side of the tree with parent "node"--->go search there 
	else if (!rel(node->info, elem))
	{
		node->left =  remove_rec(node->left, elem, rel);
		return node;
	}
}

//Komplexität : O(nrOfLevels)
Node* minimum(Node* node)
{
	//if node == nullptr don't even bother
	if (node == nullptr)
	{
		return nullptr;
	}	
	else
	{
		//search for the most left node on your tree, that's the minimum
		Node* currentNode = node;
		while (currentNode->left != nullptr)
		{
			currentNode = currentNode->left;
		}
		return currentNode;
	}
}

//Komplexität : O(nrOfLevels)
//Best case : Theta(1)
//Worst case : Theta(n)
bool SortedSet::search(TComp elem) const {
	
	if (this->isEmpty())
		return false;
	
	Node* currentNode = this->root;

	while (currentNode != nullptr)
	{
		if (currentNode->info == elem)
			return true;

		else if (rel(currentNode->info, elem))
			currentNode = currentNode->right;
		else
			currentNode = currentNode->left; 
	}
	
	return false;
}

//Komplexität : Theta(1)
int SortedSet::size() const {
	
	return this->nrElem;
}


//Komplexität : Theta(1)
bool SortedSet::isEmpty() const {
	if (this->nrElem == 0)
		return true;	
	return false;
	
}

SortedSetIterator SortedSet::iterator() const {
	return SortedSetIterator(*this);
}

//Komplexität : Theta(n)
SortedSet::~SortedSet() {
	Node* currentNode;
	while (this->nrElem != 0)
	{
		currentNode = this->root;
		currentNode = remove_rec(currentNode, currentNode->info, this->rel);
		nrElem--;
	}
}


