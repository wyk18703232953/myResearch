from collections import defaultdict
import random

def generate_test_data(n):
    # 随机生成 n 个只含 '(' 和 ')' 的字符串
    # 长度在 1~10 之间，可按需调整规模
    S = []
    for _ in range(n):
        length = random.randint(1, 10)
        s = ''.join(random.choice('()') for _ in range(length))
        S.append(s)
    return S

def solve(S):
    d1 = defaultdict(lambda: 0)
    d2 = defaultdict(lambda: 0)
    ans = 0
    for s in S:
        cum1 = 0
        flag1 = True
        for c in s:
            if c == '(':
                cum1 += 1
            else:
                cum1 -= 1
            if cum1 < 0:
                flag1 = False
        if flag1:
            ans += d2[cum1]

        cum2 = 0
        flag2 = True
        for i in reversed(range(len(s))):
            c = s[i]
            if c == ')':
                cum2 += 1
            else:
                cum2 -= 1
            if cum2 < 0:
                flag2 = False
        if flag2:
            ans += d1[cum2]

        if cum1 == 0 and cum2 == 0 and flag1 and flag2:
            ans += 1
        if flag1:
            d1[cum1] += 1
        if flag2:
            d2[cum2] += 1
    return ans

def main(n):
    S = generate_test_data(n)
    ans = solve(S)
    print(ans)

if __name__ == "__main__":
    # 示例：n = 5
    main(5)