import random

def solve_one_case(n, k, s):
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
    # 生成测试数据：
    # 1. 随机生成 q 个测试
    # 2. 对每个测试随机生成 k（1 <= k <= n）
    # 3. 随机生成长度为 n 的字符串 s，由 'R','G','B' 构成
    q = 5  # 测试组数，可根据需要修改
    colors = ['R', 'G', 'B']
    random.seed(0)

    results = []
    for _ in range(q):
        k = random.randint(1, n)
        s = ''.join(random.choice(colors) for _ in range(n))
        ans = solve_one_case(n, k, s)
        results.append((n, k, s, ans))

    # 打印输出（可按需要调整格式）
    for n_val, k_val, s_val, ans_val in results:
        print(f"n={n_val}, k={k_val}, s={s_val}, ans={ans_val}")

if __name__ == "__main__":
    main(10)