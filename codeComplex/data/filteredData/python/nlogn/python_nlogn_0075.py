import random

def main(n):
    # 生成测试数据：n 对 (manan, surbhi)；并生成 k
    # 这里假设 manan 和 surbhi 在 [1, n] 范围内，k 在 [1, n]
    pairs = [(random.randint(1, n), random.randint(1, n)) for _ in range(n)]
    k = random.randint(1, n)

    l = pairs[:]

    # 与原逻辑一致的排序：先按 manan 降序，再按 surbhi 升序（通过 -x[1] 实现）
    l.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    ans = 1
    ps = l[k - 1][0]
    tp = l[k - 1][1]

    for i in range(k, n):
        if l[i][0] == ps and l[i][1] == tp:
            ans += 1
        else:
            break

    for i in range(k - 2, -1, -1):
        if l[i][0] == ps and l[i][1] == tp:
            ans += 1
        else:
            break

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)