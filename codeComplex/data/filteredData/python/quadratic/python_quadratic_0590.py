import sys

sss = 'RGB' * 700

def check(ss, p):
    i = 0
    m = 10 ** 5
    ans = 0
    while i < len(p):
        if p[i] != sss[i]:
            ans += 1
        i += 1
    m = min(m, ans)
    ans = 0
    i = 1
    while i < len(p) + 1:
        if p[i - 1] != sss[i]:
            ans += 1
        i += 1
    m = min(m, ans)
    ans = 0
    i = 2
    while i < len(p) + 2:
        if p[i - 2] != sss[i]:
            ans += 1
        i += 1
    m = min(m, ans)
    return m

def main(n):
    # 解释规模映射：
    # n 控制单个测试中字符串长度 n 和子串长度 k 的数量级。
    # 为保持算法结构：使用单测试用例，n 为字符串长度，k = max(1, n // 2)。
    t = 1  # 单测试用例数量
    results = []
    for _ in range(t):
        str_len = max(1, n)
        k = max(1, str_len // 2)
        # 构造确定性字符串 s，使用循环模式 'RGB' 并做简单变形
        base = ('RGB' * ((str_len // 3) + 2))[:str_len]
        s_chars = []
        for i in range(str_len):
            c = base[i]
            # 简单确定性扰动：每 5 个字符翻转为下一个颜色
            if (i // 5) % 3 == 1:
                if c == 'R':
                    c = 'G'
                elif c == 'G':
                    c = 'B'
                else:
                    c = 'R'
            s_chars.append(c)
        s = ''.join(s_chars)
        m = 10 ** 5
        for i in range(str_len - k + 1):
            m = min(m, check(sss, s[i:i + k]))
        results.append(m)
    # 为保持输出行为，依次打印每个测试用例结果
    for res in results:
        print(res)

if __name__ == "__main__":
    # 示例调用：可修改 n 以进行不同规模实验
    main(10)