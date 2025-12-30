import random

def solve_case(n, k, s):
    m = 10 ** 4
    for j in range(n):
        if j + k <= n:
            l1 = ["R", "G", "B"]
            m1 = m2 = m3 = 0
            # pattern starting from offset 0
            for i in range(j, j + k):
                if l1[(i - j) % 3] != s[i]:
                    m1 += 1
            # pattern starting from offset 1
            for i in range(j, j + k):
                if l1[(i + 1 - j) % 3] != s[i]:
                    m2 += 1
            # pattern starting from offset 2
            for i in range(j, j + k):
                if l1[(i + 2 - j) % 3] != s[i]:
                    m3 += 1
            m = min(m, m1, m2, m3)
        else:
            break
    return m

def main(n):
    """
    n: problem规模，用于生成测试数据。
       我们生成 q 个测试用例，每个用例长度约为 n，
       并自动生成 k 和字符串 s。
    """
    # 生成测试用例数量
    q = max(1, n // 5)

    results = []
    for _ in range(q):
        # 随机生成该测试的 n_case 和 k
        n_case = max(1, n + random.randint(-n // 2, n // 2))
        n_case = min(max(1, n_case), max(1, n))  # 控制在 [1, n] 内
        if n_case <= 0:
            n_case = 1
        k = random.randint(1, n_case)

        # 生成随机 RGB 字符串
        chars = ['R', 'G', 'B']
        s = ''.join(random.choice(chars) for _ in range(n_case))

        res = solve_case(n_case, k, s)
        results.append((n_case, k, s, res))

    # 输出结果：每行一个测试用例的答案
    for n_case, k, s, res in results:
        print(res)

if __name__ == "__main__":
    # 你可以在此修改 n 来控制测试规模
    main(10)