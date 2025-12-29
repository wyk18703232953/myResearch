import random

def main(n: int):
    # 生成测试数据：
    # n: 数组 f 的长度
    # m: 目标值，取一个与 n 相关的较大值
    # k: 初始值，取一个相对较小值
    #
    # 为保证有一定随机性且规模由 n 控制，这里设置：
    # f[i] ∈ [1, 10]
    # k   ∈ [0, n]
    # m   ∈ [k, k + 10 * n] （确保有可能达成，也可能达不成）
    random.seed(0)  # 如需多样性可去掉固定种子

    f = [random.randint(1, 10) for _ in range(n)]
    k = random.randint(0, n)
    m = random.randint(k, k + 10 * n)

    # 以下为原始逻辑
    f.sort()

    fs = 0
    ptr = len(f) - 1
    while ptr >= 0:
        if m <= k:
            print(fs)
            return
        k -= 1
        k += f[ptr]
        fs += 1
        ptr -= 1

    if m <= k:
        print(fs)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)