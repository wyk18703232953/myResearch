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

def solve_single_case(n, k, s):
    temp = givestringsk(k)
    ans = 10000000000000
    for i in range(k, n + 1):
        for j in range(3):
            ans = min(ans, countdifferences(s[i - k:i], temp[j]))
    return ans

def generate_test_case(case_index, n):
    # 输入结构：
    # n, k 两个整数 + 一个长度为 n 的字符串 s
    # 这里将 n 作为字符串长度，k 为 1..n 中确定性的值
    k = max(1, (case_index % n) + 1) if n > 0 else 1
    pattern = "RGB"
    s_chars = []
    for i in range(n):
        s_chars.append(pattern[(i + case_index) % 3])
    s = "".join(s_chars)
    return n, k, s

def main(n):
    # 将 n 解释为：有 n 组测试，每组字符串长度也为 n
    t = n
    results = []
    for case_index in range(t):
        length = n
        if length <= 0:
            results.append(0)
            continue
        nn, kk, ss = generate_test_case(case_index, length)
        res = solve_single_case(nn, kk, ss)
        results.append(res)
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(5)