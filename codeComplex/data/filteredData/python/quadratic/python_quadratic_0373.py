def norm(x):
    return (x % 998244353 + 998244353) % 998244353

def main(n):
    # 将原来的两个输入 n, k 映射为：n 为原 n，k = n
    k = n

    dp1 = [0]
    dp2 = [0]

    for i in range(n):
        l = [1]
        cur = 0
        for j in range(n + 1):
            cur += l[j]
            if j > i:
                cur -= l[j - i - 1]
            cur = norm(cur)
            l.append(cur)
        dp1.append(l[n])
        dp2.append(norm(dp1[i + 1] - dp1[i]))

    ans = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if i * j < k:
                ans = norm(ans + dp2[i] * dp2[j])

    ans = norm(ans * 2)
    print(ans)

if __name__ == "__main__":
    main(10)