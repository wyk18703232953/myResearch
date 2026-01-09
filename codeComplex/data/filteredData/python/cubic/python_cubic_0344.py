import bisect

prime = [2]
for i in range(3, 4 * 10**3, 2):
    if i % 2 == 0:
        continue
    flag = False
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            flag = True
            break
    if not flag:
        prime.append(i)


def primefactor(num):
    index = 0
    output = []
    while num >= prime[index] ** 2:
        times = 0
        while num % prime[index] == 0:
            num = num // prime[index]
            times += 1
        if times & 1:
            output.append(prime[index])
        index += 1
    if num > 1:
        output.append(num)
    return tuple(output)


def run_single_case(n, k, arr):
    fact = {}
    left = [[0 for _ in range(k + 1)] for _ in range(n)]
    dp = [[300000 for _ in range(k + 1)] for _ in range(n)]

    stack = [0]
    for i in range(n):
        factor = primefactor(arr[i])
        if factor in fact:
            bisect.insort(stack, fact[factor] + 1)
        fact[factor] = i
        for j in range(k + 1):
            if j < len(stack):
                left[i][j] = stack[-j - 1]

    for i in range(n):
        for j in range(k + 1):
            for t in range(j + 1):
                l = left[i][t]
                if l > 0:
                    dp[i][j] = min(dp[l - 1][j - t] + 1, dp[i][j])

                else:
                    dp[i][j] = 1

    return dp[-1][-1]


def main(n):
    if n <= 0:
        return
    T = 3
    results = []
    for case in range(T):
        length = n + case
        k = max(0, n // 3 - case)
        if k > length:
            k = length
        arr = [(5 * (i + 1) + (case + 1)) for i in range(length)]
        res = run_single_case(length, k, arr)
        results.append(res)
    for value in results:
        # print(value)
        pass
if __name__ == "__main__":
    main(10)