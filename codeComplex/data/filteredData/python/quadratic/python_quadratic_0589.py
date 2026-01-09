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

def solve_one(n, k, s):
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
    return ans

def main(n):
    # 解释 n 的含义：
    # 使用多测试用例结构：
    #   q = n
    #   第 i 个测试：
    #       n_i = i + 2        (字符串长度，从 2 开始增长)
    #       k_i = (i // 2) + 1  (窗口大小，随 i 增长但不超过 n_i)
    #       s_i 为长度 n_i 的确定性字符串，按 i, 位置 j 构造
    q = n
    results = []
    for case_id in range(q):
        ni = case_id + 2
        ki = (case_id // 2) + 1
        if ki > ni:
            ki = ni
        # 确定性生成字符串 s：
        # 使用 (case_id + j) % 3 决定字符
        chars = []
        for j in range(ni):
            v = (case_id + j) % 3
            if v == 0:
                chars.append("R")
            elif v == 1:
                chars.append("G")

            else:
                chars.append("B")
        s = "".join(chars)
        res = solve_one(ni, ki, s)
        results.append(res)
    # 为了保持行为简单明了，只输出每个测试的答案
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(5)