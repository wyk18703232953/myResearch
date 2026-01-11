from collections import defaultdict

def solve_with_data(n, k, a):
    cnt = [defaultdict(lambda: 0) for _ in range(11)]
    for i in a:
        cnt[len(str(i))][i % k] += 1
    ans = 0
    d = 10
    for i in range(1, 11):
        cnti = cnt[i]
        for j in a:
            ans += cnti[(k - d * j) % k]
        d *= 10
    for i in a:
        if not int(str(i) * 2) % k:
            ans -= 1
    return ans

def main(n):
    # n: size of the input array
    # Deterministically generate k and array a of length n
    if n <= 0:
        # print(0)
        pass
        return
    k = max(1, n // 3 + 7)
    a = [(i * 1234567 + 89) % (10**9 + 7) for i in range(1, n + 1)]
    result = solve_with_data(n, k, a)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)