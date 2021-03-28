#include "L_Mihaila_Daria_AufgabeA-rational.h"
#include <vector>
#include <iostream>
#include <assert.h>

using namespace std;


void TestSet()
{
    
    Rational number;  // number = 7/3
    number.set_numerator(7);
    number.set_denominator(3);
    
    assert(number.get_denominator() == 3);
    assert(number.get_numerator() == 7);
    try
    {
        number.set_denominator(0);
        assert(false);
    }
    catch (...)
    {
        
    }
}
void TestGet()
{
    Rational number;
    number.set_numerator(4);
    number.set_denominator(7);
    assert(number.get_numerator() == 4);
    assert(number.get_denominator() == 7);
    
}

void TestSum()
{
    Rational number;  
    Rational number1; 
    Rational number2;  
    number.set_numerator(7);
    number.set_denominator(3);

    number1.set_numerator(4);
    number1.set_denominator(5);

    number2.set_numerator(7);
    number2.set_denominator(3);
    
    Rational sum = number1.add(number); 
    assert(sum.get_numerator() == 47 && sum.get_denominator() == 15);
    sum = number.add(number2);
    assert(sum.get_numerator() == 14 && sum.get_denominator() == 3);
}

void TestProduct()
{
    Rational number;
    Rational number1; 
    Rational number2; 
    number.set_numerator(7);
    number.set_denominator(3);

    number1.set_numerator(4);
    number1.set_denominator(5);

    number2.set_numerator(3);
    number2.set_denominator(-7);
    
    Rational product;
    
    product =  number.multiply(number1);
    assert(product.get_denominator() == 15 && product.get_numerator() == 28);

    product = number.multiply(number2);
    assert(abs(product.get_denominator()) == 1 && abs(product.get_numerator()) == 1);

}

void TestDivide()
{
    Rational number;  
    Rational number1; 
    Rational number2; 

    number.set_numerator(7);
    number.set_denominator(3);

    number1.set_numerator(4);
    number1.set_denominator(5);

    number2.set_numerator(7);
    number2.set_denominator(-3);

    Rational result = number.divide(number1);
    assert(result.get_denominator() == 12 && result.get_numerator() == 35);

    result = number.divide(number2);
    assert(result.get_numerator() == -1 && result.get_denominator() == 1);

    
}

void TestInverse()
{
    Rational number; 

    number.set_numerator(7);
    number.set_denominator(3);
    
    Rational inverse = number.inverse();
    assert(inverse.get_numerator() == 3 && inverse.get_denominator() == 7);
}

void TestCompare()
{
    Rational number;  
    Rational number1; 
    Rational number2; 

    number.set_numerator(1);
    number.set_denominator(2);

    number1.set_numerator(2);
    number1.set_denominator(4);

    number2.set_numerator(1);
    number2.set_denominator(10);

    int result = number.compare(number1);
    assert(result == 0);

    result = number.compare(number2);
    assert(result == 1);
    
    result = number2.compare(number);
    assert(result == -1);
}

void TestAll()
{
   
    TestSet();
    cout << "TestSet passed" << endl;
    TestGet();
    cout << "TestGet passed" << endl;
    TestSum();
    cout << "TestSum passed" << endl;
    TestProduct();
    cout << "TestProduct passed" << endl;
    TestDivide();
    cout << "TestDivide passed" << endl;
    TestInverse();
    cout << "TestInverse passed" << endl;
    TestCompare();
    cout << "TestCompare passed" << endl;

    
    cout << "Tests passed" << endl;
}

int main()
{
    TestAll();
     Rational number;  
    Rational number1;
    Rational number2;  
    Rational number3;  
    number.set_numerator(7);
    number.set_denominator(3);

    number1.set_numerator(4);
    number1.set_denominator(5);

    number2.set_numerator(7);
    number2.set_denominator(2);
    
    number3.set_numerator(-7);
    number3.set_denominator(3);

    Rational Array[] {number, number1, number2, number3};
    int size = sizeof(Array) / sizeof(number);
    Rational sum = Array[0];
    
    for (int i = 1; i < size; i++)
    {
       sum = sum.add(Array[i]).reduce();  
    }
    cout << "sum:  " <<sum.get_numerator() << '/' << sum.get_denominator() <<endl;
    return 0; 
}