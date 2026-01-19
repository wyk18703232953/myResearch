import math

def main(n):
    if n < 1:
        n = 1
    x = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    y = ''.join('+' if i % 3 == 0 else '?' if i % 3 == 1 else '-' for i in range(n))
    goal = x.count('+') - y.count('+')
    options = y.count('?')
    if options == 0:
        if goal == options:
            print(1)
        else:
            print(0)
    else:
        if goal > options:
            print(0)
        else:
            if goal < 0:
                print(0)
            else:
                print(math.factorial(options) / math.factorial(goal) / math.factorial(options - goal) / (2 ** options))

if __name__ == "__main__":
    main(10)