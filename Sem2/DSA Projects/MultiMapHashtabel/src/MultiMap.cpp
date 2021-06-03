#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;


MultiMap::MultiMap() {
	this->m =5;
	this->nrElems = 0;
	this->Elements = new Node*[m];
	
	for (int i = 0; i < m; i++)
	{
		this->Elements[i] = nullptr;
	}
}
//
int MultiMap::h(TKey c) const
{
	return abs(c % this->m);
}

//Komplexitat : Teta(1) amortizat
void MultiMap::add(TKey c, TValue v) {
	int pos = this->h(c);
	
	Node* newNode = new Node;
	newNode->elem.first = c;
	newNode->elem.second = v;
	newNode->next = nullptr;
	if ((nrElems / m) > 0.9)
	{
		this->rehash();
	}

	if (Elements[pos] == nullptr) // nu am niciun element cu cheia respectiva in tabela
	{
		Elements[pos] = newNode;
	}
	else
	{
		newNode->next = Elements[pos];
		Elements[pos] = newNode;
	}
	this->nrElems++;
}


//Komplexitat : Teta(nrElems)
void MultiMap::rehash()
{
	//cazul in care nrElem/m > 1.2
	
	this->m = nearest_prim(2*m);
	Node** NewElements = new Node*[m];
	
	for (int i = 0; i < m; i++)
	{
		NewElements[i] = nullptr;
	}

	int index = 0;
	while(Elements[index] == nullptr)
	{
		index++;
	}
	//am ajuns la primul element gasit in tabela

	int pos;
	Node* currentNode = Elements[index];
	 // will be the node added to the new tabel and makes sure I can continue with my currentNode in the original tabel
	
	int count = 0;//numara cate elemente am adaugat 
	while (count < nrElems)
	{
		
		if (currentNode != nullptr) 
		{
			Node* currentNodeaux = new Node;
			currentNodeaux->elem.first = currentNode->elem.first;
			currentNodeaux->elem.second = currentNode->elem.second; //dau atributiile la o copie
			currentNodeaux->next = nullptr;

			pos = this->h(currentNodeaux->elem.first);//ii gasesc locul in tabela noua dupa cheie
			
			if (NewElements[pos] == nullptr)//nu am pe pozitia aia nimic
			{	
				NewElements[pos] = currentNodeaux;
				
			}
			else //bag currentNodeaux la inceputul SLL ului de pe pos aia
			{
				currentNodeaux->next = NewElements[pos];
				NewElements[pos] = currentNodeaux;
			}
			
			count++;
				currentNode = currentNode->next; 
			//am mai transferat un element din tabela veche in aia noua
		}
		else//am dat de un nullptr trec la elementul urmator din tabela noua
		{
			index++;
			while(Elements[index] == nullptr)
				index++;
			currentNode = Elements[index];
		}
	}
	this->Elements = NewElements;
}

//Komplexitat : Teta(1)
bool MultiMap::remove(TKey c, TValue v) {
	
	//daca search nu returneaza un vector gol atunci 100% gasesc cheia respectiva in tabela
	//not so sure about the value
	if (search(c) != vector<TValue>())
	{
		int pos = this->h(c);
		Node* currentNode = Elements[pos];
		
		if (currentNode->elem.first == c && currentNode->elem.second == v)
		{
			Elements[pos] = currentNode->next;
			delete currentNode;
			this->nrElems--;
			return true;
		}
		while (currentNode->next != nullptr)
		{
			if (currentNode->next->elem.first == c && currentNode->next->elem.second == v)
				break;
			currentNode = currentNode->next;
		}
		//cand iese din while currentNode e ori nullptr ori pointeaza la prima aparitie a cheiei c

		//ori am dat de ce trebuie ori am dat de belea
		if (currentNode->next != nullptr)  //am dat de ce trebuia
		{
			if (currentNode->next->next == nullptr) // trebuie sters ultimul element din SLL 
			{	
				delete currentNode->next;
				currentNode->next = nullptr;
				this->nrElems--;
				return true;
			}
			
			Node* aux = currentNode->next;
			currentNode->next = aux->next;
			delete aux;
			this->nrElems--;
			return true;
		}
	}
	
	
	return false;
}

//Komplexitat : O(1 + nrElems/m)
vector<TValue> MultiMap::search(TKey c) const {
	if (!this->isEmpty())
	{

		vector<TValue> found_values;
		int pos = this->h(c);
		Node* currentNode = Elements[pos];
		while (currentNode != nullptr && currentNode->elem.first != c)
		{
			currentNode = currentNode->next;
		}
		//cand iese din while currentNode e ori nullptr ori pointeaza la prima aparitie a cheiei c
		if (currentNode != nullptr)
		{
			while (currentNode != nullptr)
			{
				if (currentNode->elem.first == c)
					found_values.push_back(currentNode->elem.second);
				currentNode = currentNode->next;
			}
			return found_values;
		}
	}
	return vector<TValue>();
}


int MultiMap::size() const {
	return this->nrElems;
	return 0;
}


bool MultiMap::isEmpty() const {
	if (this->nrElems == 0)
		return true;
	return false;
}

MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}
bool MultiMap::prim(int x)
{
    if ((x == 1) || (x == 0))
    {
        return false;
    }
    else if (x == 2)
    {
        return true;
    }
    else if (x % 2 == 0)
    {
            return false;
    }
    else
    {
        for (int i = 3; i<= trunc(sqrt(x)); i++ )
        {
            if (x % i == 0)
            {
                return false;
            }
        }
        return true;
    }
}

int MultiMap::nearest_prim(int cap)
{
	while (!prim(cap)) 
	{
		if (cap % 2 == 0)
			
			cap++;
		else
			cap += 2;
	}
	return cap;
}



MultiMap::~MultiMap() {
	int i = 0;
	for (; i< m ; i++)
	{
		if (Elements[i] != nullptr)
		{
			Node* current = Elements[i];
			Node* aux = current->next;
			while (aux != nullptr)
			{
				delete current;
				current = aux;
				aux = aux->next;
			}
		}
	}
	delete[] Elements;
}

