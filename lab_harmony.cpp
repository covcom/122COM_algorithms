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
    vector< tuple<int,int,int> > tests {{42, 69, 25}, 
                                        {123, 999, 50},
                                        {255, 254, 88},
                                        {127, 128, 0},
                                        {255, 126, 75},
                                        {515, 3, 100},
                                        {2147483647, 255, 100} };

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