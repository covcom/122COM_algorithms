import sys

class Morseifier:
    # MAKE AS MANY CHANGES TO THE CLASS AS YOU WANT

    def translate(self,text):
        # COMPLETE ME
        return 

    def untranslate(self,morse):
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
            print('Error! translating %s' % text)
            print('Yours  : "%s"' % yourMorse)
            print('Correct: "%s"' % morse)
            errors += 1

        if yourText != text:
            print('Error! untranslating %s' % morse)
            print('Yours  : "%s"' % yourText)
            print('Correct: "%s"' % text)
            errors += 1

    if errors == 0:
        print('Congratulations, no errors')
        print('-.-. --- -. --. .-. .- - ..- .-.. .- - .. --- -. ... / -. --- / . .-. .-. --- .-. ...')
    else:
        print('Uh oh, %d error/s remain' % errors)
        print('..- .... / --- .... / . .-. .-. --- .-. ... / .-. . -- .- .. -.')

if __name__ == '__main__':
    sys.exit(main())
