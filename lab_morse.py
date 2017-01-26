import sys

class Morseifier:
    # MAKE AS MANY CHANGES TO THE CLASS AS YOU WANT

    def translate(self,text):
        ''' A function that takes a string as input and 
            translates it into morse code before returning it '''
        # COMPLETE ME
        return 

    def untranslate(self,morse):
        ''' A function  that takes a string as input and
            translates it from morse code before returning it '''
        # COMPLETE ME
        return



























def main():
    m = Morseifier()

    tests = [('MORSE CODE','-- --- .-. ... . / -.-. --- -.. .'),
            ('INSPECTOR MORSE','.. -. ... .--. . -.-. - --- .-. / -- --- .-. ... .'), \
            ('',''), \
            ('LAST OF THE MORSICANS','.-.. .- ... - / --- ..-. / - .... . / -- --- .-. ... .. -.-. .- -. ...')]

    errors = 0
    for text, morse in tests:
        yourMorse = m.translate(text)
        yourText = m.untranslate(morse)

        if yourMorse != morse:
            print('Error when translating {}'.format(text))
            print('Yours  : "{}"'.format(yourMorse))
            print('Correct: "{}"'.format(morse))
            print()
            errors += 1

        if yourText != text:
            print('Error when translating {}'.format(morse))
            print('Yours  : "{}"'.format(yourText))
            print('Correct: "{}"'.format(text))
            print()
            errors += 1

    if errors == 0:
        print('Congratulations, no errors')
        print('-.-. --- -. --. .-. .- - ..- .-.. .- - .. --- -. ... / -. --- / . .-. .-. --- .-. ...')
    else:
        print('Uh oh, {} error/s remain'.format(errors))
        print('..- .... / --- .... / . .-. .-. --- .-. ... / .-. . -- .- .. -.')

    return errors

if __name__ == '__main__':
    sys.exit(main())
