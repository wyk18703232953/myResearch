def main(n):
    from collections import Counter

    # Map n to k and string length
    k = max(1, min(26, n // 2))
    length = max(k, n)

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Deterministically generate s of length `length`
    s = ''.join(alpha[i % k] for i in range(length))

    c = Counter(s)
    mn = 10 ** 9
    for ch in alpha[:k]:
        mn = min(mn, c[ch])
    result = mn * k
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(1000)