from collections import Counter
import copy

def solve(a, b):
    count = 0
    if a == b:
        return 1
    while a != 0 and b != 0:
        if a < b:
            count += (b // a)
            b -= a * (b // a)

        else:
            count += a // b
            a -= b * (a // b)
    return count

def main(n):
    results = []
    for i in range(1, n + 1):
        a = i
        b = 2 * i + 1
        results.append(solve(a, b))
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)