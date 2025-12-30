from math import ceil
import random

def mismatch(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt

def solve_one_case(n, k, s):
    check = ''
    for _ in range(ceil((k + 2) / 3)):
        check += 'RGB'
    patterns = [check[i:i + k] for i in range(3)]
    res = n
    for i in range(n - k + 1):
        window = s[i:i + k]
        for p in patterns:
            res = min(res, mismatch(window, p))
    return res

def main(n):
    random.seed(0)
    T = 5  # 固定生成 5 组测试数据
    results = []

    for _ in range(T):
        if n < 1:
            n = 1
        k = random.randint(1, n)
        s = ''.join(random.choice('RGB') for _ in range(n))
        results.append(solve_one_case(n, k, s))

    for ans in results:
        print(ans)

if __name__ == "__main__":
    main(10)