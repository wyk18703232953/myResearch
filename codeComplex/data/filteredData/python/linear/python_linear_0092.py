import random
import string


def main(n: int):
    # 生成测试数据：长度为 n 的随机字符串，字符从小写字母中选取
    # 保证至少有 1 个不同字符
    if n <= 0:
        return
    alphabet = string.ascii_lowercase
    s = ''.join(random.choice(alphabet) for _ in range(n))

    # 原逻辑开始
    u_set = set()
    for ch in s:
        u_set.add(ch)
    u_cnt = len(u_set)

    d = {}
    j = 0
    ans = 10**9
    for i in range(n):
        while len(d.keys()) < u_cnt and j < n:
            d[s[j]] = d.get(s[j], 0) + 1
            j += 1

        if len(d.keys()) == u_cnt:
            if j - i < ans:
                ans = j - i
        elif j == n:
            break

        d[s[i]] -= 1
        if d[s[i]] == 0:
            del d[s[i]]

    print(ans)


if __name__ == '__main__':
    # 示例：调用 main(100)
    main(100)