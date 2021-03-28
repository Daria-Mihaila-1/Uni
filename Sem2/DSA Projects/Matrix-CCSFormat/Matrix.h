#pragma once

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM 0

class Matrix {
/*
ADT Matrix –repräsentiertals schwachbesetze Matrix (sparse) in dem Compressed Column StorageFormat(CCS)mithilfe von dynamischen Arrays
*/
private:
	
	//int nrLines, nrColumns;  //nr linii + coloane din Matrix	
	int capacity;  //capacitatea matrixului
	int Nr_Elements;  // nr de elemente
	int *ArrRows;  // vector dinamic de ind linii
	int *ArrCColumns;  // vector dinamic de ind compressed columns
	TElem *Values;  //vectorul de valori
	int nr_lines;
	int nr_columns;
	int ArrCColumnsSize; 

	

public:
	
	~Matrix()
	{
		delete[] this->ArrRows;
		delete[] this->ArrCColumns;
		delete[] this->Values;
	}

	//constructor
	Matrix(int nrLines, int nrCols);

	//returns the number of lines
	int nrLines() const;

	//returns the number of columns
	int nrColumns() const;

	//returns the element from line i and column j (indexing starts from 0)
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem element(int i, int j) const;

	//modifies the value from line i and column j
	//returns the previous value from the position
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem modify(int i, int j, TElem e);
	
	//inserts a non zero value on line i column j 
	// "index" is the index at which the value e and its line index will be inserted in Values rspct. ArrRows
	void Insert(int line, int column, int index, TElem e);

	//removes the element from line and column and replaces it with a 0 in the matrix
	void Remove(int line, int column, int index);
	
	//capacity will be doubled
	//copyies the rows array in a new bigger dynamic array
	//returns new array
	void Resize(char text);

	void ResizeMat(int nrLines, int nrCols);

};