l, r = map(int, input().split())

print(0 if l == r else 2 ** len(bin(l ^ r)[2:]) - 1)