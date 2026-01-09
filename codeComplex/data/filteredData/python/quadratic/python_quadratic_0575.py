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

def solve_single(n, k, s):
    temp = givestringsk(k)
    ans = 10**18
    for i in range(k, n + 1):
        for j in range(3):
            ans = min(ans, countdifferences(s[i - k:i], temp[j]))
    return ans

def main(n):
    # n 表示字符串长度规模，同时设置 k 与测试组数 T
    # 为保持可规模化和确定性：
    #  - T = 3（固定三组测试）
    #  - 对第 t 组测试，使用不同的 k
    #  - 字符串 s 由周期 "RGB" 再加简单扰动构造
    if n <= 0:
        return

    T = 3
    results = []

    for t in range(T):
        length = n
        k = max(1, min(length, 1 + (t * length) // (T + 1)))

        base_pattern = ["R", "G", "B"]
        s_list = []
        for i in range(length):
            ch = base_pattern[i % 3]
            if (i + t) % 5 == 0:
                if ch == "R":
                    ch = "G"
                elif ch == "G":
                    ch = "B"

                else:
                    ch = "R"
            s_list.append(ch)
        s = "".join(s_list)

        res = solve_single(length, k, s)
        results.append(res)

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)