#include "L3_Mihaila_Daria_DSM.h"
#include <exception>
#include <iostream>
//names : vector
// el_count : int
//matrix : int** dynamic array 2D


DSM::DSM(int count)
{
    this->el_count = count;
    
    //defining the matrix
    matrix = new int*[el_count];  //actually a dynamic vector of vectors
    for(int i = 0; i< el_count; i++)
    {
        matrix[i] = new int[el_count];
    }

    for (int i = 0; i < el_count; i++)
    {
        for (int j = 0; j < el_count; j++)
        {    
            matrix[i][j] = 0;
        }
    }

    this->names.resize(el_count); 
    
}

//the second constructor 
DSM::DSM(vector<string> name_elements)
{
    this->names = name_elements;
    this->el_count = names.size();
    matrix = new int*[el_count];
    for(int i = 0; i< el_count; i++)
    {
        matrix[i] = new int[el_count];
    }
    
    for (int i = 0; i < el_count; i++)
    {
        for (int j = 0; j < el_count; j++)
        {    
            matrix[i][j] = 0;
        }
    }
}

//copy constructor
DSM::DSM(const DSM& obj)
{
    el_count = obj.el_count;
    vector <string> element_names = obj.names;
    int** m = obj.matrix;

}

//returns he number of names found in the names vector
int DSM::size()
{
    return (this->el_count);
}

//setter for an element of the names vector
void DSM::set_element_name(int index, string name)
{
    if (index < 0 || index > this->el_count)
        throw exception();
    this->names[index] = name;
}
//returns the name on the index "index" of the names vector 
string DSM::get_name(int index)
{
    if (index < 0 || index > this->el_count)
        throw exception();
    return this->names[index];
}

//creates a new matrix that has another line and column of 0s added to make space for the new name that has links
void DSM::resize()
{
    el_count++;
    int** new_matrix =  new int*[el_count];
    
    for (int i = 0; i < el_count; i++)
    {
        new_matrix[i] = new int[el_count];
    }

    for (int i = 0; i < el_count; i++)
    {
        for (int j = 0; j < el_count; j++)
        {    
            if (i<el_count -1 && j<el_count-1)
                new_matrix[i][j] = matrix[i][j];
            else 
                new_matrix[i][j] = 0;
        }
    }
    
    this->matrix = new_matrix;
   
}

//adds a non-zero value to the from_element line and to_element column
void DSM::add_link(string from_element, string to_element, int weight)
{
    if (weight <=0 || from_element == to_element)
        throw exception();
    
    int index_from = -1;
    int index_to = -1;
    
    for (int i = 0; i < el_count; i++)
    {
        if (this->names[i] == from_element)
        {
            index_from = i;
        }
        else if ( this->names[i] == to_element)
        {   
            index_to = i;
        }
        if (index_from != -1 && index_to != -1)
            break;
    }
    
    if (index_from == -1)
    {
        this->names.push_back(from_element);
        resize();
        index_from = el_count-1;
    }
    else if (index_to == -1)
    {
        names.push_back(to_element);
        resize();
        index_to = el_count-1;
    }
    
    this->matrix[index_from][index_to] = weight;
}

//looks for a non-zero value on the line of the from_element and the column of the to_element 
bool DSM::have_link(string from_element, string to_link)
{
    int index_from = -1;
    int index_to = -1; 

    for (int i = 0; i < el_count; i++)
    {
        if (names[i] == from_element)
        {
                index_from = i;
        }

        if (names[i] == to_link)
        {    
            index_to = i;
        }
        if (index_from != -1 && index_to != -1)
                break;
            
    }
    if (index_from != -1 && index_to != -1)
    {
       
        if (matrix[index_from][index_to] != 0)
        {
                       
            return true;
        }
    }
    
    return false;
    
}
//sets the value of the element found on the line of the from_element and the column of the to_element to 0
void DSM::delete_link(string from_element, string to_element)
{
    int from_index = -1;
    int to_index = -1;

    for (int i = 0; i< el_count; i++)
    {
        if (names[i] == from_element)
            from_index = i;
        if (names[i] == to_element)
            to_index = i;
    }
    
    if (from_index == -1 || to_index == -1)
    { 
        cout << "Elements not included in the vector"<< endl;
        throw exception();
    }
    else
    {
        matrix[from_index][to_index] = 0;
    }
}

//returns the value found on the line of the from_element(1) and the line of the to_link(2), where the weight of the link from 1->2 is stored 
int DSM::link_weight(string from_element, string to_link)
{
    int from_index = -1;
    int to_index = -1;
    
    for (int i = 0; i< el_count; i++)
    {
        if (names[i] == from_element)
            from_index = i;
        if (names[i] == to_link)
            to_index = i;
    }
    if (from_index == -1 || to_index == -1)
    {
        cout << "Elements not included in the vector"<< endl;
        throw exception();
    }
    else
    {
        return matrix[from_index][to_index];    
    }
}

//on the line of the matrix with the index of element_name are found all the links that element_name has to other names 
int DSM::count_to_links(string element_name)
{
    int index = -1;
    for(int i =0; i < el_count; i++)
    {
        if (element_name ==names[i])
        {   index = i;
            break;
        }
    } 
    if (index ==-1)
    {
        cout << "Element not found" << endl;
        throw exception();
    }
    else
    {
        int link_count = 0;
        for (int j = 0; j < el_count; j++)
            link_count += matrix[index][j];
        return link_count;
    }
}

//on the column of the matrix with the index of element_name are found all the links that element_name has from other names
int DSM::count_from_links(string element_name)
{
    int index = -1;
    for(int i =0; i < el_count; i++)
    {
        if (element_name == names[i])
        {  
            index = i;
            break;
        }
    } 
    if (index ==-1)
    {
        cout << "Element not found" << endl;
        throw exception();
    }
    else
    {
        int link_count = 0;
        for (int i = 0; i < el_count; i++)
            link_count += matrix[i][index];
        return link_count;
    }
}

//like an adiacency matrix for an oriented graph the matrix has a value only once for a link, there are no duplicates
int DSM::count_all_links()
{
    int c = 0;
    for (int i = 0; i< el_count ; i++)
    {
        for (int j = 0; j< el_count; j++)
        {    
            if (matrix[i][j] != 0)
            c +=1;
        } 
    }
    return c;
}

//using the previous method, the function calculates the ratio between the number of all the links found and the number of all possible links  
double DSM::calculate_matrix_density()
{
    int ratio= this->count_all_links()/el_count*el_count;

    return ratio;
}
//destructor
//destroyes all its "under-pointers" and the pointer to them
DSM::~DSM()
{
    for(int i = 0; i< el_count; i++)
        delete matrix[i];
    delete[] matrix;
}