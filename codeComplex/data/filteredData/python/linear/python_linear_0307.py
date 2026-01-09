import math

def main(n):
    a = [(i * 3 + 5) for i in range(n)]
    x = 10**9 + 2
    y = 0
    for i in range(n):
        val = math.ceil((a[i] - i) / n) * n + i + 1
        if x > val:
            x = val
            y = i + 1
    # print(y)
    pass
if __name__ == "__main__":
    main(10)