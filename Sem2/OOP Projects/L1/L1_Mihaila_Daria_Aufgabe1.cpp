#include <iostream>
#include <cmath>
using namespace std;
 
// a)
//Funktion untersucht ob eine Zahl x eine Primzahl ist
bool prim(int x)
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

// Funktion druckt alle Primzahlen < n 
void PrimzKleinerAls(int n)
{
    cout << "Primzahlen kleiner wie n:";
    for (int i = 2; i < n; i++)
    {
        if (prim(i))
        {
            cout << i << ' ';
        }
    }
    cout << endl;
}

//b)
//Funktion druckt die langste ansteigende Teilfolge eines Vektors
void langsteTeilfolge(int vec[], int len)
{
    int lokal_length = 1;  // eine lokale Lange
    int length_max = 0;
    int anf_index = 0;
    int anf_indexmax = 0;  // die maximale Lange, Anfangsindex der Teilfolge mit der lokalen Lange und Anfangsindex der Teilfolge mit der maximalen Lange  
    
    for (int i = 0; i < len - 1; i++ )
    {
        if (vec[i] < vec[i+1])
        {
            if (lokal_length == 1)
            { 
                anf_index = i;
            }
            lokal_length += 1;
        }
        else
        {
            lokal_length = 1;
        }
        if (lokal_length > length_max)
        {
            length_max = lokal_length;
            anf_indexmax = anf_index;
        }
    }
    cout << "Die langste ansteigende Teilfolge des Vektors ist:";
    for (int i = anf_indexmax ; i < anf_indexmax + length_max; i++)
    {
        cout << vec[i] << ' ';
    }
    cout << endl;
}
int main()
{
    //a)Tests
    int n;
    cout << "n=";
    cin >> n ; 

    PrimzKleinerAls(n);
    
    //b)Tests
    int v[] = {8, 7, 10, 8, 7, 9, 9, 9, 9}; 
    int v1[] = {8, 7, 10, 8, 7, 9, 11, 12, 113, 26}; 
    
    int size = sizeof(v) / sizeof(v[0]);
    int size1 = sizeof(v1) / sizeof(v[0]);

    langsteTeilfolge(v, size);
    langsteTeilfolge(v1, size);
    
    return 0;
}