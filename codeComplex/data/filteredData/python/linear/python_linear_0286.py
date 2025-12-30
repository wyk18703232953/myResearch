from collections import defaultdict
import random

def num(s):
    l, r = 0, 0
    for ch in s:
        if l == 0 and ch == ")":
            r += 1
        elif ch == "(":
            l += 1
        elif l and ch == ")":
            l -= 1
    return (l, r)

def f(mp, cnt):
    ans = 0
    for l in cnt:
        if l.count(0) < 1:
            continue
        if l != (0, 0) and l == l[::-1]:
            continue
        t = mp[l[::-1]]
        ans += t
        if t and l != l[::-1]:
            mp[l] -= 1
    return ans

def generate_test_data(n, seed=0):
    """
    生成 n 个仅含 '(' 和 ')' 的随机字符串。
    长度在 [1, 2*n] 范围内（可根据需要调整）。
    """
    random.seed(seed)
    strings = []
    for _ in range(n):
        length = random.randint(1, max(2, 2 * n))
        s = ''.join(random.choice("()") for _ in range(length))
        strings.append(s)
    return strings

def main(n):
    """
    n 为规模：生成 n 个测试括号串并计算结果。
    返回与原程序相同的最终整数输出。
    """
    test_strings = generate_test_data(n)

    cnt = []
    mp = defaultdict(int)
    for s in test_strings:
        l = num(s)
        cnt.append(l)
        mp[l] += 1

    return f(mp, cnt)

if __name__ == "__main__":
    # 示例：运行 main(5) 查看结果
    print(main(5))