def f(l):
    n, m = l
    return ['5' * 282, '4' * 281 + '5']

def main(n):
    l = [n, n]
    res = f(l)
    for r in res:
        print(r)
    return res

if __name__ == "__main__":
    main(10)