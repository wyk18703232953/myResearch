import random

def main(n: int):
    # 生成测试数据：n 个区间 [l, r]，且 l <= r
    # 这里生成在 [1, 10*n] 范围内的随机区间
    src = []
    for i in range(n):
        l = random.randint(1, 10 * n)
        r = random.randint(l, 10 * n)
        src.append((l, r, i))

    # 原逻辑开始
    src.sort()  # 按 (l, r, i) 字典序排序

    prev_l = max_r = 0
    prev_i = outer = -1
    for l, r, i in src:
        if prev_l == l:
            print(prev_i + 1, i + 1)
            return
        if r <= max_r:
            print(i + 1, outer + 1)
            return
        else:
            max_r = r
            outer = i
        prev_l = l
        prev_i = i
    print(-1, -1)


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)