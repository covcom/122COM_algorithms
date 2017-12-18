#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

int harmony( int a, int b )
{
    return 0;
}





















int main()
{
    vector< tuple<int,int,int> > tests {make_tuple(42, 69, 25), 
                                        make_tuple(123, 999, 50),
                                        make_tuple(255, 254, 88),
                                        make_tuple(127, 128, 0),
                                        make_tuple(255, 126, 75),
                                        make_tuple(515, 3, 100),
                                        make_tuple(2147483647, 255, 100) };

    int errors = 0;
    for( auto test : tests )
    {
        int yourAnswer = harmony( get<0>(test), get<1>(test) );
        
        if( yourAnswer != get<2>(test) )
        {
            cout << "Error when comparing " << get<0>(test) << " and " << get<1>(test) << endl
                << "Yours  : " << yourAnswer << endl
                << "Correct: " << get<2>(test) << endl
                << endl;
            errors += 1;
        }
    }

    if( errors == 0)
    {
        cout << "Congratulations, no errors" << endl;
    }
    else
    {
        cout << "Uh oh, " << errors << " error/s remain" << endl;
    }

    return errors;
}