import random

def main(n):
    # 生成测试数据
    # 约束条件：1 <= l <= r，x >= 0
    # 题意通常为：选择若干题目，其难度和在 [l, r]，且最大难度与最小难度差至少为 x
    # 这里随机生成一组合理数据
    random.seed(0)

    # 生成难度数组 C，长度为 n
    # 为了避免过大数字，难度值设为 1 ~ 1000
    C = [random.randint(1, 1000) for _ in range(n)]

    total_sum = sum(C)
    min_c = min(C)
    max_c = max(C)

    # 合理生成 l, r, x
    # l 在 [0, total_sum] 内
    l = random.randint(0, total_sum // 2)
    # r 在 [l, total_sum] 内
    r = random.randint(l, total_sum)
    # x 在 [0, max_c - min_c] 内
    x = random.randint(0, max_c - min_c if max_c > min_c else 0)

    k = 0
    for i in range(1 << n):
        W = [w for w, b in zip(C, bin(i)[2:].zfill(n)) if b == '1']
        if not W:
            continue
        s = sum(W)
        if l <= s <= r and max(W) - min(W) >= x:
            k += 1

    print(k)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)