import sys

def main(n):
    # n defines the number of following (f, t) pairs
    # s is deterministically derived from n
    s = n // 2 + 1
    maxi = s
    for i in range(n):
        f = i
        t = (i * 2) % (n + 3)
        maxi = max(maxi, f + t)
    print(maxi)

if __name__ == "__main__":
    main(10)