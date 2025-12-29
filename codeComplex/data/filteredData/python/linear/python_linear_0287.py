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
        t = mp[l[::-1]]
        ans += t
        if t and l != l[::-1]:
            mp[l] -= 1
    return ans

def generate_string():
    # 随机生成一条括号串
    length = random.randint(1, 20)
    return ''.join(random.choice("()") for _ in range(length))

def main(n):
    # n 为字符串数量规模
    random.seed(0)
    cnt = []
    mp = defaultdict(int)
    for _ in range(n):
        s = generate_string()
        l = num(s)
        cnt.append(l)
        mp[l] += 1
    result = f(mp, cnt)
    print(result)

if __name__ == "__main__":
    # 示例：可以修改这里的 n 测试规模
    main(10)