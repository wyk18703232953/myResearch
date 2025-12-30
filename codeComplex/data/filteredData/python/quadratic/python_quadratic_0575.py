import random

def givestringsk(k):
    t = ["R", "G", "B"]
    ans = []
    for i in range(3):
        temp = ""
        for j in range(i, i + k):
            temp += t[j % 3]
        ans.append(temp)
    return ans

def countdifferences(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

def solve_one_case(n, k, s):
    patterns = givestringsk(k)
    ans = 10**18
    for i in range(k, n + 1):
        segment = s[i - k:i]
        for p in patterns:
            ans = min(ans, countdifferences(segment, p))
    return ans

def main(n):
    # 生成测试数据：随机选择 k，随机生成长度为 n 的 RGB 字符串
    if n <= 0:
        return []

    # k 在 1 到 n 之间
    k = random.randint(1, n)
    chars = ["R", "G", "B"]
    s = "".join(random.choice(chars) for _ in range(n))

    # 若需要多组测试，可自行调整 cases 数量
    cases = [(n, k, s)]

    results = []
    for n_case, k_case, s_case in cases:
        res = solve_one_case(n_case, k_case, s_case)
        print(res)
        results.append(res)

    return results