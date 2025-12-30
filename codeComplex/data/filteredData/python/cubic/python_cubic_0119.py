import random
import string

def solve2(s, t, left, right):
    n = len(s)
    m = len(t)
    nuxt = [-1] * (left + 1)
    nuxt[0] = 0

    for i in range(n):
        for j in reversed(range(left + 1)):
            k = nuxt[j]
            if k == -1:
                continue
            if j != left:
                if s[i] == t[j]:
                    nuxt[j + 1] = max(nuxt[j + 1], k)
            if k != right:
                if s[i] == t[left + k]:
                    nuxt[j] = max(nuxt[j], k + 1)
    return nuxt[-1] == right

def single_case(s, t):
    m = len(t)
    for i in range(m + 1):
        if solve2(s, t, i, m - i):
            return "YES"
    return "NO"

def main(n):
    # 生成 n 组测试数据
    # 每组中：
    #   |s| 在 [1, n] 内
    #   |t| 在 [1, min(n, |s|)] 内
    # 字符从小写字母中随机生成
    random.seed(0)

    results = []
    for _ in range(n):
        len_s = random.randint(1, n)
        len_t = random.randint(1, len_s)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))
        results.append(single_case(s, t))

    # 输出所有结果（每组一行）
    for r in results:
        print(r)

if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)