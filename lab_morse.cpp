#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

class Morseifier
{
    // MAKE AS MANY CHANGES TO THE CLASS AS YOU WANT

public:
    Morseifier()
    {
    }

    /* A function that takes a string as input and 
        translates it into morse code before returning it */
    string translate( string text )
    {
        string answer = "";

        return answer;
    }

    /* A function  that takes a string as input and
        translates it from morse code before returning it */
    string untranslate( string morse )
    {
        string answer = "";
        
        return answer;
    }
};


























int main()
{
    Morseifier m;

    vector< tuple<string, string> > tests { make_tuple("MORSE CODE","-- --- .-. ... . / -.-. --- -.. ."),
                                            make_tuple("INSPECTOR MORSE",".. -. ... .--. . -.-. - --- .-. / -- --- .-. ... ."), 
                                            make_tuple("",""), 
                                            make_tuple("LAST OF THE MORSICANS",".-.. .- ... - / --- ..-. / - .... . / -- --- .-. ... .. -.-. .- -. ...") };

    int errors = 0;
    for( auto test : tests )
    {
        string yourMorse = m.translate( get<0>(test) );
        string yourText = m.untranslate( get<1>(test) );

        if( yourMorse != get<1>(test) )
        {
            cerr << "Error when translating " << get<0>(test) << endl << 
                    "Yours  : \"" << yourMorse << "\"" << endl <<
                    "Correct: \"" << get<1>(test) << "\"" << endl << endl;
            errors += 1;
        }

        if( yourText != get<0>(test) )
        {
            cerr << "Error when translating " << get<1>(test) << endl << 
                    "Yours  : \"" << yourText << "\"" << endl << 
                    "Correct: \"" << get<0>(test) << "\"" << endl << endl;
            errors += 1;
        }
    }

    if( errors == 0 )
    {
        cout << "Congratulations, no errors" << endl << 
                "-.-. --- -. --. .-. .- - ..- .-.. .- - .. --- -. ... / -. --- / . .-. .-. --- .-. ..." << endl;
    }
    else
    {
        cout << "Uh oh, " << errors << " error/s remain" << endl << 
                "..- .... / --- .... / . .-. .-. --- .-. ... / .-. . -- .- .. -." << endl;
    }

    return errors;
}

