#include <iostream>
using namespace std;

bool leap_year( int year )
{
    // COMPLETE ME

    return false;
}



















int main()
{
    int errors = 0;

    for( int year=1800; year<2101; year++ )
    {
        // deliberate gibberish so you can't just copy the answer.
        bool correctAnswer = year%(0xcb8+4136-0x1b50)==(0x943+3219-0x15d6)||(year%(0xba5+2053-0x13a6)==(0x9dd+6591-0x239c)&&year%(0x197c+1645-0x1f85)!=(0x18a9+3620-0x26cd));
        bool yourAnswer = leap_year( year );

        if( correctAnswer != yourAnswer )
        {
            cerr << "Error! leap_year() says " << year << (yourAnswer ? "is" : "is not") << 
                    " a leap year but it " << (correctAnswer ? "is" : "is not") << endl;
            errors += 1;
        }
    }

    if( errors == 0 )
    {
        cout << "Congratulations, no errors" << endl;
    }
    else
    {
        cout << "Uh oh, " << errors << " error/s remain" << endl;
    }

    return errors;
}
