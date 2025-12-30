import random

def gen(n, b):
    a = [(x + b) % 3 for x in range(n)]
    s = ""
    for i in range(n):
        if a[i] == 0:
            s += "R"
        if a[i] == 1:
            s += "G"
        if a[i] == 2:
            s += "B"
    return s

def main(n):
    # 生成测试数据：固定 k，随机字符串 s
    # 这里设 k 为 n 的一半（至少为 1，至多为 n）
    if n <= 0:
        return 0

    k = max(1, n // 2)
    colors = ['R', 'G', 'B']
    s = ''.join(random.choice(colors) for _ in range(n))

    ans = n
    for xi in range(3):
        t = gen(n, xi)
        diff = 0
        for i in range(k):
            if s[i] != t[i]:
                diff += 1
        ans = min(ans, diff)
        for j in range(k, n):
            if s[j - k] != t[j - k]:
                diff -= 1
            if s[j] != t[j]:
                diff += 1
            ans = min(ans, diff)
    # 按原程序行为，仅输出结果
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：可自行修改 n 进行快速测试
    main(10)