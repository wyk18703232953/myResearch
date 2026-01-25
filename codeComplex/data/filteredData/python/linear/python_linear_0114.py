from math import ceil

def main(n):
    N = n
    S = (N * (N + 1)) / 2
    F = int(ceil(N / 2.0))
    ans = int((S + F) / 2)
    print(ans)

if __name__ == "__main__":
    main(10)