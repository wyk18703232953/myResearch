import bisect

prime = [2]
for i in range(3, 4 * 10 ** 3, 2):
    flag = False
    if i % 2 == 0:
        continue
    for j in range(3, int(i ** 0.5) + 1, 2):
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


def main(n):
    T = n
    for r in range(T):
        size = n
        k = max(0, n // 10)
        arr = [i + 2 for i in range(size)]

        fact = {}
        left = [[0 for _ in range(k + 1)] for _ in range(size)]
        dp = [[300000 for _ in range(k + 1)] for _ in range(size)]

        stack = [0]
        for i in range(size):
            factor = primefactor(arr[i])
            if factor in fact:
                bisect.insort(stack, fact[factor] + 1)
            fact[factor] = i
            for j in range(k + 1):
                if j < len(stack):
                    left[i][j] = stack[-j - 1]

        for i in range(size):
            for j in range(k + 1):
                for t in range(j + 1):
                    l = left[i][t]
                    if l > 0:
                        dp[i][j] = min(dp[l - 1][j - t] + 1, dp[i][j])

                    else:
                        dp[i][j] = 1

        # print(dp[-1][-1])
        pass
if __name__ == "__main__":
    main(10)