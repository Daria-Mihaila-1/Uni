#include <vector>
#include "L3_Mihaila_Daria_DSM.h"
#include "assert.h"
#include<iostream>
using namespace std;

void TestSize()
{
    cout << "TestSize: " ;
    DSM matrix(8);
    assert(matrix.size() == 8);
    vector <string> vec{"Audi","Toyota"};
    DSM matrix1(vec);
    assert(matrix1.size() == 2);
    cout << "Passed"<<endl;
}


void TestNames()
{
    cout << "testNames: ";
    
    DSM matrix(8);
    
    for (int i = 0; i< matrix.size(); i++)
    {
        matrix.set_element_name(i, "Audi");
    }
    
    matrix.set_element_name(0, "Volkswagen");
    assert(matrix.get_name(1) =="Audi");
    assert(matrix.get_name(0) == "Volkswagen");
    matrix.set_element_name(2, "Bentley");
    assert(matrix.get_name(2) == "Bentley");
    matrix.set_element_name(3, "Lamborghini");
    assert(matrix.get_name(3) == "Lamborghini");

    
    cout << "Passed" << endl;
}

void TestAddHaveLink()
{
    
    cout << "TestAddHaveLink: "<< endl;;
    DSM matrix(3);
    matrix.set_element_name(0, "Volkswagen");
    matrix.set_element_name(1, "Audi");
    assert(matrix.get_name(1) =="Audi");
    matrix.set_element_name(2, "Lamborghini");
    assert(matrix.get_name(2) =="Lamborghini");

    try
    {
        matrix.add_link("Volkswagen", "Audi", -1);   
    }    
    catch (...)
    {
        cout <<"Sorry, the weight must be > 0" << endl;
    }
    
    matrix.add_link("Volkswagen", "Audi", 5);   
    
    assert(matrix.have_link("Volkswagen", "Audi"));
    matrix.add_link("Audi", "Volkswagen", 10);
    assert(matrix.have_link("Audi", "Volkswagen"));
    matrix.add_link("Volkswagen", "Bentley", 89);
    assert(matrix.have_link("Volkswagen", "Bentley"));
    matrix.add_link("SEAT", "Volkswagen", 8);
    assert(matrix.have_link("SEAT", "Volkswagen"));
    cout <<"TestAddHaveLink: Passed"<< endl;

}


void TestLinkWeight()
{
    cout << "TestLinkWeight: ";
    vector <string> vec{"Audi","Toyota", "Opel", "Nissan"};
    DSM matrix(vec);

    try
    {
        cout << matrix.link_weight("Outsider", "Other Outsider");
    }
    catch(const std::exception& e){};
    
    try
    {
        matrix.link_weight("Audi", "Outsider");
    }
    catch(const std::exception& e)
    {}

    try
    {
        cout << matrix.link_weight("Outsider","Toyota");
    }
    catch(const std::exception& e)
    {}
    matrix.add_link("Toyota", "Audi", 89);
    assert(matrix.link_weight("Toyota", "Audi") == 89);
    cout << "Passed" << endl;
}


void TestDelete()
{
    cout << "Test Delete: ";
    vector <string> vec{"Audi","Toyota", "Opel", "Nissan"};
    DSM matrix(vec);
    
    matrix.add_link("Opel", "Nissan",67);
    assert(matrix.link_weight("Opel", "Nissan") == 67);
    matrix.delete_link("Opel", "Nissan");
    assert(matrix.have_link("Opel", "Nissan") == false);
    try
    {
        matrix.delete_link("Outsider", "Nissan");
    }
    catch(const std::exception& e)
    {
        
    }
    assert(matrix.link_weight("Opel", "Nissan") == 0);
    
    cout << "Passed" << endl;
}


void TestToLinks()
{
    cout << "TestToLinks: ";
    vector <string> vec{"Audi","Toyota", "Opel", "Nissan"};
    DSM matrix(vec);
    matrix.add_link("Audi","Toyota",1);
    matrix.add_link("Audi","Opel",1);
    matrix.add_link("Audi","Nissan", 1);
    matrix.add_link("Audi", "Suzuki", 1);
    assert(matrix.count_to_links("Audi") == 4);

    try
    {
        cout << matrix.count_to_links("Outsider");
    }
    catch(const std::exception& e)
    {}
    

    cout << "Passed" << endl;
}


void TestFromLinks()
{
    cout << "TestFromLinks: ";
    vector <string> vec{"Audi","Toyota", "Opel", "Nissan"};
    DSM matrix(vec);
    matrix.add_link("Toyota","Audi",1);
    matrix.add_link("Opel","Audi",1);
    matrix.add_link("Nissan","Audi",1);
    matrix.add_link("Suzuki","Audi" ,1);
    assert(matrix.count_from_links("Audi") == 4);
    
    try
    {
        cout << matrix.count_to_links("Outsider");
    }
    catch(const std::exception& e)
    {}

    cout << "Passed" << endl;
}

void TestMatrixDensityLinkCount()
{
    cout << "Test TestMatrixDensity + LinkCount: ";
    vector <string> vec{"Audi","Toyota", "Opel", "Nissan"};
    DSM matrix(vec);
    matrix.add_link("Toyota","Audi",1);
    matrix.add_link("Opel","Audi",1);
    matrix.add_link("Nissan","Audi",1);
    matrix.add_link("Suzuki","Audi" ,2);
    assert(matrix.calculate_matrix_density() == 1/4);

    cout << "Passed" << endl;
}

int main(){
    
    TestSize();
    TestNames();
    TestAddHaveLink();
    TestDelete();
    TestLinkWeight();
    TestToLinks();
    TestFromLinks();
    TestMatrixDensityLinkCount();
    cout << "End"<< endl;

    return 0;
}