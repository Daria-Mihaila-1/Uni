#include <iostream>
#include "L_Mihaila_Daria_AufgabeA-rational.h"
#include <cmath>
using namespace std;


//getter denominator
const int Rational::get_denominator()
{
    return denominator;
}

//getter numerator
const int Rational::get_numerator()
{
    return numerator;
}
//setter numerator
void Rational::set_numerator(int nr)
{
    numerator = nr;
}

//setter numerator
void Rational::set_denominator(int nr)
{
    if (nr == 0)
    {
        throw exception();
    }
    denominator = nr;
}

Rational Rational::reduce()
//Zahl : n/m
{
    int n;
    n = numerator;
    int m;
    m = denominator;
    Rational answer;
    if (abs(m) == abs(n))
    {
        answer.denominator = denominator/m;
        answer.numerator = numerator/m;
        return answer;
    }
    else
    { 
        n = abs(n);
        m = abs(m);
        while (m != n)
        {
            if (n > m)
            {
                n -= m; 
            }
            else
            {
                m -= n;
            }
        }
        answer.numerator = numerator / n;
        answer.denominator = denominator / n;
        
        if (answer.denominator < 0 && answer.numerator < 0)
        {   answer.numerator = abs(answer.numerator);
            answer.denominator = abs(answer.denominator); 
        }
        return answer;
    }
        
}

Rational Rational::inverse()
{
    Rational answer;
    answer.denominator = numerator;
    answer.numerator = denominator;
    return answer;
}

int Rational::compare(Rational obj)
{
    if (numerator* obj.denominator < obj.numerator* denominator)
    {
        return -1;
    }
    else if (numerator* obj.denominator > obj.numerator* denominator)
    {
        return 1;
    }
    else return 0;
}

Rational Rational::operator+(Rational obj)

{
    return add(obj);
}

Rational Rational::operator-(Rational obj)
{
    Rational answer;
    if (denominator == obj.denominator)
    {
        answer.numerator = numerator - obj.numerator;
        answer.denominator = denominator;
    }
    else
    {
        answer.denominator = denominator * obj.denominator;
        answer.numerator = numerator * obj.denominator - obj.numerator * denominator;  
    }

    return answer.reduce();
}

Rational Rational::operator/(Rational obj)
{
    Rational answer;
    if (abs(numerator) == abs(obj.numerator) && abs(denominator) == abs(obj.numerator))
    {
        answer.denominator = denominator / obj.denominator;
        answer.numerator = numerator / obj.numerator;
        return answer;
    }
    answer.numerator = numerator * obj.denominator;
    answer.denominator = denominator * obj.numerator;
    return answer.reduce();
}

Rational Rational::operator*(Rational obj)
    {
        Rational answer;
        answer.numerator = numerator * obj.numerator;
        answer.denominator = denominator * obj.denominator;
        return answer.reduce();
    }


//addition with return = result
Rational Rational::add(Rational obj)
{
        Rational answer;
        if (denominator == obj.denominator)
        {
            answer.numerator = numerator + obj.numerator;
            answer.denominator = denominator;
        }
        else
        {
            answer.denominator = denominator * obj.denominator;
            answer.numerator = numerator * obj.denominator + obj.numerator * denominator;  
        }
     
        return answer.reduce();
}


//subtraction with return = result
Rational Rational::subtract(Rational obj)
{
    Rational answer;
    if (denominator == obj.denominator)
    {
        answer.numerator = numerator - obj.numerator;
        answer.denominator = denominator;
    }
    else
    {
        answer.denominator = denominator * obj.denominator;
        answer.numerator = numerator * obj.denominator - obj.numerator * denominator;  
    }

    return answer.reduce();
}


//division with return = result
Rational Rational::divide(Rational obj)
{
    Rational answer;
    if (abs(numerator) == abs(obj.numerator) && abs(denominator) == abs(obj.numerator))
    {
        answer.denominator = denominator / obj.denominator;
        answer.numerator = numerator / obj.numerator;
        return answer;
    }
    answer.numerator = numerator * obj.denominator;
    answer.denominator = denominator * obj.numerator;
    return answer.reduce();
}


//multiplication with return = result  
Rational Rational::multiply(Rational obj)
    {
        Rational answer;
        answer.numerator = numerator * obj.numerator;
        answer.denominator = denominator * obj.denominator;
        return answer.reduce();
    }
