import random


def solve(a):
    n = len(a)
    b = []
    c = []
    e = []
    for i in range(n):
        if a[i] == 1:
            b.append(i)
    for i in range(n):
        if a[i] != 1:
            c.append([a[i], i])
    if not c:
        return "NO\n"
    ans = len(c)
    for i in range(len(c) - 1):
        e.append((c[i][1], c[i + 1][1]))
        c[i][0] -= 1
        c[i + 1][0] -= 1
    if b:
        e.append((b[-1], c[-1][1]))
        c[-1][0] -= 1
        b.pop()
        ans += 1
    if b:
        e.append((b[-1], c[0][1]))
        c[0][0] -= 1
        b.pop()
        ans += 1
    i = 0
    while b:
        while i < len(c) and c[i][0] == 0:
            i += 1
        if i == len(c):
            return "NO\n"
        e.append((b[-1], c[i][1]))
        c[i][0] -= 1
        b.pop()

    out_lines = []
    out_lines.append(f"YES {ans - 1}")
    out_lines.append(str(len(e)))
    for x, y in e:
        out_lines.append(f"{x + 1} {y + 1}")
    return "\n".join(out_lines) + "\n"


def gen_test_data(n):
    # 生成一个长度为 n 的数组 a，包含 1 和大于等于 2 的整数
    # 保证至少有一个非 1 元素以避免必然 NO 的平凡情况
    if n == 1:
        # 单独处理：随机给一个 >=2，或1（可能输出NO）
        if random.random() < 0.7:
            return [random.randint(2, 5)]
        else:
            return [1]
    a = []
    # 先生成至少一个非 1
    non_one_pos = random.randint(0, n - 1)
    for i in range(n):
        if i == non_one_pos:
            a.append(random.randint(2, 5))
        else:
            # 大多数为 1，少量为 [2,5]
            if random.random() < 0.7:
                a.append(1)
            else:
                a.append(random.randint(2, 5))
    return a


def main(n):
    a = gen_test_data(n)
    result = solve(a)
    # 输出测试数据和结果，方便验证
    print(n)
    print(" ".join(map(str, a)))
    print(result, end="")


if __name__ == "__main__":
    # 示例：使用 n=5 运行一次
    main(5)