import random

def solve_one(n, k, s):
    min_ans = 10 ** 9
    pr1 = [0]
    pr2 = [0]
    pr3 = [0]
    for i in range(n):
        count1 = count2 = count3 = 0
        if i % 3 == 0:
            if s[i] != "R":
                count1 += 1
            if s[i] != "G":
                count2 += 1
            if s[i] != "B":
                count3 += 1
        elif i % 3 == 1:
            if s[i] != "G":
                count1 += 1
            if s[i] != "B":
                count2 += 1
            if s[i] != "R":
                count3 += 1
        else:  # i % 3 == 2
            if s[i] != "B":
                count1 += 1
            if s[i] != "R":
                count2 += 1
            if s[i] != "G":
                count3 += 1

        pr1.append(pr1[-1] + count1)
        pr2.append(pr2[-1] + count2)
        pr3.append(pr3[-1] + count3)

        j = i + 1
        if j >= k:
            c1 = pr1[j] - pr1[j - k]
            c2 = pr2[j] - pr2[j - k]
            c3 = pr3[j] - pr3[j - k]
            min_ans = min(min_ans, c1, c2, c3)
    return min_ans


def main(n):
    # 生成测试：q 个测试用例
    # 这里令 q 与 n 相关，也可以改为固定值
    q = max(1, n // 5)

    results = []
    colors = ['R', 'G', 'B']
    rng = random.Random(0)

    for _ in range(q):
        # 为每个测试生成 n_i, k_i, s
        # n_i 在 [1, n] 内随机，k_i 在 [1, n_i] 内随机
        ni = rng.randint(1, n)
        ki = rng.randint(1, ni)
        s = ''.join(rng.choice(colors) for _ in range(ni))

        res = solve_one(ni, ki, s)
        results.append(res)

    print(*results, sep="\n")


if __name__ == "__main__":
    # 示例：调用 main，规模为 20
    main(20)