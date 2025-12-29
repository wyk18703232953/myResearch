import random

def main(n: int):
    # 1. 生成测试数据
    # 根据规模 n 生成两个整数 l, r
    # 这里约定：0 <= l, r < 2^n
    if n <= 0:
        l, r = 0, 0
    else:
        upper = 1 << n
        l = random.randrange(upper)
        r = random.randrange(upper)

    # 2. 原始逻辑：求 l 和 r 在二进制上最左侧不同位所覆盖的最大值（全1掩码）
    target, final = l ^ r, 1
    while target:
        target >>= 1
        final <<= 1
    result = final - 1

    # 输出结果（可根据需要也输出 l, r 便于调试）
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10) 测试规模为 2^10 以内的随机 l, r
    main(10)