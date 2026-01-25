def main(n):
    # n: length of the array a
    if n <= 0:
        return 0

    p = n + 7  # deterministic choice of p based on n
    a = [(i * 3 + 1) % (p + 5) for i in range(n)]

    forward = [a[0]]
    for i in range(1, n):
        forward.append(forward[-1] + a[i])
    sm = sum(a)
    mx = -float('inf')
    for i in range(n - 1):
        mx = max(mx, (forward[i] % p) + ((sm - forward[i]) % p))
    return mx


if __name__ == "__main__":
    # example call
    result = main(10)
    print(result)