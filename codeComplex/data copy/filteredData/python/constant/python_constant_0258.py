n = 10
pos = 5
l = 3
r = 7

def main(n):
    pos = n // 2 + 1
    l = max(1, n // 3)
    r = min(n, 2 * n // 3 + 1)
    if l == 1 and r == n:
        # print(0)
        pass
    elif l == 1:
        # print(abs(pos - r) + 1)
        pass
    elif r == n:
        # print(abs(pos - l) + 1)
        pass

    else:
        # print(min(abs(pos - l), abs(pos - r)) + abs(l - r) + 2)
        pass
if __name__ == "__main__":
    main(10)