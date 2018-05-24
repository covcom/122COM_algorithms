import sys

def harmony( a, b ):
    # convert to binary
    aBinary = [int(x) for x in bin(a)[2:]]
    bBinary = [int(x) for x in bin(b)[2:]]

    # pad/trim lists to length of 8
    aBinary = [0]*8 + aBinary
    bBinary = [0]*8 + bBinary

    aBinary = aBinary[-8:]
    bBinary = bBinary[-8:]

    # how many bits match
    count = 0
    for i in range(8):
        if aBinary[i] == bBinary[i]:
            count += 1

    # figure out percentage
    return int(round(count / 8 * 100,0))






















def main():
    tests = [(42, 69, 0), \
            (123, 999, 50), \
            (255, 254, 88), \
            (127, 128, 0), \
            (255, 126, 75), \
            (515, 3, 100), \
            (2147483647, 255, 100)]

    errors = 0
    for a, b, correct in tests:
        yourAnswer = harmony( a, b )
        
        if yourAnswer != correct:
            print('Error when comparing {} and {}'.format(a, b))
            print('Yours  : {}'.format(yourAnswer))
            print('Correct: {}'.format(correct))
            print()
            errors += 1

    if errors == 0:
        print('Congratulations, no errors')
        
    else:
        print('Uh oh, {} error/s remain'.format(errors))

    return errors

if __name__ == '__main__':
    sys.exit(main())