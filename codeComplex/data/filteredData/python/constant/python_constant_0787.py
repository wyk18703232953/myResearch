from math import sqrt

def issq(p):
    x = int(sqrt(p))
    return x * x == p

def g(n):
    return (issq(n // 2) and n % 2 == 0) or (issq(n // 4) and n % 4 == 0)

def f(n):
    return "YES" if g(n) else "NO"

def main(n):
    results = []
    for i in range(1, n + 1):
        results.append(f(i))
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)