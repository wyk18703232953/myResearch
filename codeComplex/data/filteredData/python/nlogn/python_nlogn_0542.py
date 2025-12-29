from collections import Counter

def main(n):
    # 这里根据 n 生成测试数据：
    # 约定：k 取一个和 n 有关的正整数，数组 lst 为前 n 个正整数
    k = n + 7 if n > 0 else 1  # 防止 k 为 0
    lst = list(range(1, n + 1))

    lst2 = []
    for i in range(n):
        lst2.append(((lst[i] % k), len(str(lst[i]))))

    dp = [[] for _ in range(12)]
    for mod_val, length in lst2:
        dp[length].append(mod_val)

    for i in range(12):
        if dp[i]:
            dp[i] = Counter(dp[i])

    ans = 0
    for i in lst:
        for j in range(2, 12):
            v1 = ((i % k) * pow(10, j - 1, k)) % k
            need = (k - v1) % k
            if isinstance(dp[j - 1], Counter) and need in dp[j - 1]:
                ans += dp[j - 1][need]

    for i in lst:
        if int(str(i) + str(i)) % k == 0:
            ans -= 1

    print(ans)


# 示例调用
if __name__ == "__main__":
    main(10)