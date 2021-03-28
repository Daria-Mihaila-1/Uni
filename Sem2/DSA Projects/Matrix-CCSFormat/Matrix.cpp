#include "Matrix.h"
#include <exception>
#include <iostream>
using namespace std;



Matrix::Matrix(int nrLines, int nrCols) 
{
	if ((nrLines <= 0) || (nrCols <= 0))
	{
		throw exception();
	} 
	this->nr_lines = nrLines;
	this->nr_columns = nrCols;
	this->Nr_Elements = 0;
	this->capacity = 10; //capacitatea pt toate array-urile
	this->ArrCColumnsSize = nr_columns+1;

	this->ArrRows = new int[capacity];
	this->ArrCColumns = new int[nr_columns+1];
	this->Values = new TElem[capacity];

	for (int i = 0; i < ArrCColumnsSize; i++)
	{
		this->ArrCColumns[i] = 0;
	}	
}

//Komplexität : Teta(1) 
int Matrix::nrLines() const {

	return nr_lines;
}

//Komplexität : Teta(1)
int Matrix::nrColumns() const {
	
	return nr_columns;
}

//Komplexität : O(n) 
//Best case : Teta(1) 
//	-findet eine Exception
//	-das gesuchte Element ist das Erste
//Worst case : O(n)
//	-das gesuchte Element befindet sich nicht in der Matrix und die Funktion gibt NULL_TELEM zurück 
TElem Matrix::element(int i, int j) const 
{
	if (i < 0 || j < 0 || i >= this->nr_lines || j >= this->nr_columns)
	{
		throw exception();
	}
	
	int row;
	for (int pos = ArrCColumns[j]; pos < ArrCColumns[j+1]; pos++)
	{
		row = this->ArrRows[pos];
		if (row == i)
		{
		
			return Values[pos];
		} 
		else if (row > i)
		{
			break;
		}
	}
	return NULL_TELEM;
}

//Komplexität : O(nrCols+1)
// Worst case : Teta(nrCols+1)
//Best case : Teta(1) 
//	-die Arrays werden abgehackt
void Matrix::ResizeMat(int nrLines, int nrCols)
{
	if (nrCols > this->nr_columns)
	{
		
		int *NewArrCColumns = new int [nrCols+1];
		
		for(int index = 0; index < nrCols+1; index++)
		{
			NewArrCColumns[index] = ArrCColumns[index];
		}
		ArrCColumnsSize = nrCols+1;
		this->ArrCColumns = NewArrCColumns;
	}
	else //se taie din matrice atunci ma duc doar pana la nrCols+1 in ArrCColumns
	{//ma duc pana la nrCols +2 ca sa pot copia in arrRows+values nou si elementele de pe ultima coloana
		
		this->Nr_Elements = ArrCColumns[nrCols+1];
		this->ArrCColumnsSize = nrCols+1;
	}
	this->nr_lines = nrLines;
	this->nr_columns = nrCols;
	
}
//Komplexität : Teta(n)
void Matrix::Resize(char message)
{
	int *NewArrRows;
	TElem* NewValues;
	
	if (message == 'g')
		this->capacity *= 2;
	else 
		this->capacity /= 2;
	
	NewArrRows = new int[capacity];
	
	NewValues = new int[capacity];
	
	for(int i = 0; i < Nr_Elements; i++)
	{
		NewArrRows[i] = ArrRows[i];
		NewValues[i] = Values[i]; 
	}
	this->ArrRows = NewArrRows;
	this->Values = NewValues;
}

//Komplexität : O(n)
//Best case : O(1)
//	-das letzte Element muss entfernt werden
//Worst case : O(n)
//	-das erste Element muss entfernt werden 
void Matrix::Remove(int line, int column, int index)
{
	for(int pos = index + 1; pos < Nr_Elements; pos++)
	{
		ArrRows[pos-1] = ArrRows[pos];
		Values[pos-1] = Values[pos];
	}

	Nr_Elements--;

	for (int pos = column + 1; pos < ArrCColumnsSize; pos++)
	{
		ArrCColumns[pos]--;
	}
}

//Komplexität : O(n)
//Best case : O(1)
//	-das Element soll am Ende des Array's eingefugt werden
//Worst case : O(n)
//	-das Element soll am Anfang des Array's eingefugt werden
void Matrix::Insert(int line, int column, int index, TElem e)
{
	this->Nr_Elements++;
	
	for (int pos = Nr_Elements ; pos > index; pos--)
	{
		ArrRows[pos] = ArrRows[pos-1];
		Values[pos] = Values[pos-1];
	}
	
	ArrRows[index] = line;
	Values[index] = e;

	
	for (int pos = column + 1; pos < ArrCColumnsSize; pos++)
	{
		ArrCColumns[pos]++;
	}

}
//Komplexität :  O(n)
//Best case : Teta(1)
//	-exception thrown
//Worst case : O(n)
TElem Matrix::modify(int i, int j, TElem e) {
	
	if (i < 0 || j < 0 || i >= this->nr_lines || j >= this->nr_columns)
	{
		throw exception();
	}
	TElem el;
	int row = -1;
	int pos = ArrCColumns[j]; 
	for (; pos < ArrCColumns[j+1]; pos++)  //parcurge toti indexii din ArrRows 
	{
		row = ArrRows[pos];  //indexi de pe linie al elementelor 
		
		if (row >= i)
		{
			break;
		}
	}

	if (row != i) // pozitia i, j nu e in array-uri
	{
		if (e != 0)
		{
			if (this->Nr_Elements == this->capacity)
			{
				Resize('g');
			}
			
			int index = ArrCColumns[j]; //index din ArrRows al primului index de pe coloana j 
			
			while (ArrRows[index] < i && index < ArrCColumns[j+1])
			{
				index++;
			}
			el = Values[index];
			Insert(i, j, index, e);
			
			return el;
			
		}	
	}
	else
	{
		
		if (e != 0)
		{
			el = Values[pos];
			this->Values[pos] = e;
			return el;
		}
		else
		{
			int index = this->ArrCColumns[j];
			 //index din ArrRows al primului index de pe coloana j 
			while (ArrRows[index] < i && index < ArrCColumns[j+1])
			{
				index++;
			}
			if (Nr_Elements == this->capacity / 4)
				Resize('s');  
			Remove(i, j, index);	
		}
	}
	return NULL_TELEM;
}


