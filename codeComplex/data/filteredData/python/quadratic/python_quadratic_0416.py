def main(n):
    import random
    import string

    # 生成测试数据：
    # 随机选择 k，1 <= k <= n
    # 随机生成长度为 n 的字符串 s（小写字母+数字）
    k = random.randint(1, n)
    alphabet = string.ascii_lowercase + string.digits
    s = ''.join(random.choice(alphabet) for _ in range(n))

    ans = ""
    # 原代码逻辑：给定 n,k,s，构造满足条件的字符串
    for i in range(len(s) + 1, 0, -1):
        res = s
        end = s[-i:]
        for _ in range(k - 1):
            res += end
        cnt = 0
        for j in range(len(res) - len(s) + 1):
            if res[j:j + len(s)] == s:
                cnt += 1
        if cnt == k:
            ans = res
            break  # 找到后可以提前结束

    print(ans)


if __name__ == "__main__":
    # 可以在此处指定规模 n 进行调用
    main(5)