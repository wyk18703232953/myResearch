import random

def solve_single_case(n, k, s):
    R = G = B = 0
    ans = float('inf')
    for j in range(n):
        if j % 3 == 0:
            if s[j] == 'R':
                G += 1
                B += 1
            elif s[j] == 'G':
                R += 1
                B += 1
            else:
                R += 1
                G += 1
        elif j % 3 == 1:
            if s[j] == 'R':
                G += 1
                R += 1
            elif s[j] == 'G':
                G += 1
                B += 1
            else:
                R += 1
                B += 1
        else:
            if s[j] == 'R':
                R += 1
                B += 1
            elif s[j] == 'G':
                R += 1
                G += 1
            else:
                G += 1
                B += 1

        if j >= k - 1:
            ans = min(ans, R, G, B)
            idx = j - k + 1
            if idx % 3 == 0:
                if s[idx] == 'R':
                    G -= 1
                    B -= 1
                elif s[idx] == 'G':
                    R -= 1
                    B -= 1
                else:
                    R -= 1
                    G -= 1
            elif idx % 3 == 1:
                if s[idx] == 'R':
                    G -= 1
                    R -= 1
                elif s[idx] == 'G':
                    G -= 1
                    B -= 1
                else:
                    R -= 1
                    B -= 1
            else:
                if s[idx] == 'R':
                    R -= 1
                    B -= 1
                elif s[idx] == 'G':
                    R -= 1
                    G -= 1
                else:
                    G -= 1
                    B -= 1
    return ans

def main(n):
    # 生成测试数据：q 个测试
    q = 5
    random.seed(0)
    answers = []
    for _ in range(q):
        # 生成 k：1 到 n 之间
        k = random.randint(1, n)
        # 生成长度为 n 的 RGB 字符串
        s = ''.join(random.choice('RGB') for _ in range(n))
        ans = solve_single_case(n, k, s)
        answers.append(ans)
    # 输出每个测试的答案
    for a in answers:
        print(a)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)