using namespace std;

class Rational  
{
    //private
    int numerator; // Zahler
    int denominator;  //Nenner
       
    public:
    Rational()
    {
        numerator = 0;
        denominator = 1;
    }
    
    int const get_numerator();

    int const get_denominator();

    void set_numerator(int nr);

    void set_denominator(int nr);

    Rational add(Rational obj);

    Rational  subtract(Rational obj);

    Rational multiply(Rational obj);

    Rational divide(Rational obj);
    
    Rational reduce();

    Rational inverse();

    int compare(Rational obj);

    Rational operator+(Rational obj);

    Rational operator-(Rational obj);
    
    Rational operator*(Rational obj);
    
    Rational operator/(Rational obj);
    
    ~Rational()
    {
           
    }
  
};