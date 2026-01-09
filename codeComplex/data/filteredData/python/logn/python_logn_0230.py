def bigNumber(n, s):
    for i in range(s, n + 1):
        sumVal = 0
        num = i
        while num:
            sumVal += num % 10
            num //= 10
        if i - sumVal >= s:
            # print(n - i + 1)
            pass
            return
    # print(0)
    pass

def main(n):
    # Deterministic mapping from n to original (n, s)
    # Ensure s <= n to keep behavior meaningful
    N = n
    if N < 1:
        N = 1
    S = N // 2  # example: s is set to half of n deterministically
    bigNumber(N, S)

if __name__ == "__main__":
    main(10)