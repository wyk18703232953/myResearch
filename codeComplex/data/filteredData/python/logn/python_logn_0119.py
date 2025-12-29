from random import randint

def main(n: int):
    """
    根据规模 n 生成一组测试数据 (l, r)，并执行原始逻辑：
    给定 l, r，求满足条件的最大值（原代码的输出）。
    这里生成方式：
    - 保证 1 <= l <= r <= 2^n - 1
    - n 也作为位数上限的控制参数。
    """
    if n <= 0:
        return

    # 生成测试数据：位数不超过 n 的正整数
    max_val = (1 << n) - 1
    l = randint(1, max_val)
    r = randint(l, max_val)

    # 原始核心逻辑：对单组 (l, r) 进行计算并打印结果
    if len(bin(l)) < len(bin(r)):
        ans = (1 << len(bin(r)[2:])) - 1
    else:
        p = bin(l)[2:]
        q = bin(r)[2:]
        rr = 0
        for i in range(len(q)):
            if p[i] != q[i]:
                rr = len(p) - i
                break
        ans = (1 << rr) - 1
    print(ans)


if __name__ == "__main__":
    # 示例：可自行修改 n 规模
    main(10)