def main(n):
    if n <= 0:
        return 0
    a = [(i * 1234567 + 890123) % 1000000007 for i in range(1, n + 1)]
    difficulty = a[0]
    expectation = a[0] % 998244353
    for i in range(1, n):
        expectation = expectation * 2 + difficulty + a[i]
        difficulty = difficulty * 2 + a[i]
        expectation %= 998244353
        difficulty %= 998244353
    # print(expectation)
    pass
    return expectation

if __name__ == "__main__":
    main(10)