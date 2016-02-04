import sys
import calendar

def leap_year(year):
    # COMPLETE ME

    return False

def main():
    errors = 0
    for year in range(1800,2101):
        correctAnswer = calendar.isleap(year)
        yourAnswer = leap_year(year)

        if correctAnswer != yourAnswer:
            print('Error! leap_year() says %d %s a leap year but it %s' % (year, 'is' if yourAnswer else 'is not', 'is' if correctAnswer else 'is not'))
            errors += 1

    if errors == 0:
        print('Congratulations, no errors')
    else:
        print('Uh oh, %d error/s remain' % errors)

if __name__ == '__main__':
    sys.exit(main())