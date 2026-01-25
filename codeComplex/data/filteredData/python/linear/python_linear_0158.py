from collections import defaultdict

def main(n):
    dct = defaultdict(int)
    lst = [0] * n
    for i in range(n):
        a = i + 1
        b = (2 * i + 3)
        c = (i % 5) + 1
        x = (a + b) / c
        lst[i] = x
        dct[x] += 1
    for i in lst:
        print(dct[i], end=' ')


if __name__ == "__main__":
    main(10)