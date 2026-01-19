import math
def main():
    x = input()
    y = input()
    goal = x.count('+') - y.count('+')
    options = y.count('?')
    if options == 0:
        if goal == options:
            print(1)
        else:
            print(0)
    else:
        if (goal > options):
            print(0)
        else:
            if goal < 0:
                print(0)
            else:
                print(math.factorial(options)/math.factorial(goal)/math.factorial(options-goal)/(2**options))
main()
