import random
import string

def main(n: int):
    # 生成测试数据：长度为 n 的字符串 S
    # 为保证逻辑有意义，字符集大小在 [1, min(26, n)] 之间
    if n <= 0:
        print(0)
        return

    k = random.randint(1, min(26, n))
    chars = random.sample(string.ascii_lowercase, k)
    S = ''.join(random.choice(chars) for _ in range(n))

    # 原逻辑开始
    M = {}

    N = n
    s = set()
    for c in S:
        s.add(c)
        M[c] = 0

    i = 0
    j = -1
    aux = 0
    ans = 10**10

    while j < N - 1:
        j += 1
        M[S[j]] += 1
        if M[S[j]] == 1:
            aux += 1
        while M[S[i]] > 1:
            M[S[i]] -= 1
            i += 1
        if aux == len(s):
            ans = min(ans, j - i + 1)

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 20
    main(20)