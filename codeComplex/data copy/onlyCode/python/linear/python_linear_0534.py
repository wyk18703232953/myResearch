from collections import Counter


if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input()
    c = Counter(s)
    min_symbols = min(c[chr(ord("A") + i)] for i in range(k))
    print(min_symbols * k)
