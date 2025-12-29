import random

def main(n):
    # 生成测试数据
    # 随机生成 l, r, x 和 C（题目规模参数为 n）
    # 为了保证有意义：生成 C 后再设定 l, r, x

    # 随机生成题目中各值的上限
    MAX_C = 10**3  # 单个题目难度上限，可按需调整

    # 生成 n 个题目难度
    C = [random.randint(1, MAX_C) for _ in range(n)]

    total_sum = sum(C)
    min_C = min(C)
    max_C = max(C)

    # 生成 l, r，保证 0 <= l <= r <= total_sum
    l = random.randint(0, total_sum)
    r = random.randint(l, total_sum)

    # 生成 x，0 <= x <= max_C - min_C
    x = random.randint(0, max_C - min_C if max_C > min_C else 0)

    # 原始逻辑
    k = 0
    for i in range(2 ** n):
        W = [w for w, b in zip(C, bin(i)[2:].zfill(n)) if b == '1']
        if not W:
            continue
        s = sum(W)
        if l <= s <= r and max(W) - min(W) >= x:
            k += 1

    print(k)


if __name__ == "__main__":
    # 示例：调用 main，传入规模 n
    main(10)