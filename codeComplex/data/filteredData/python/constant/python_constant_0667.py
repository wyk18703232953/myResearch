import random

def oracle(a, b, x, y):
    """模拟交互：返回 (a^x) ? (b^y)，结果为 '1' 表示 (a^x) > (b^y)，否则 '0'。"""
    return '1' if (a ^ x) > (b ^ y) else '0'

def main(n):
    """
    n 为规模参数，这里用于控制 a, b 的取值范围：0 <= a, b < 2^n 且 n <= 29。
    返回算法推断出的 (a, b) 以及真实的 (a, b) 以便验证。
    """
    if n <= 0:
        raise ValueError("n 必须为正整数")
    if n > 29:
        raise ValueError("此算法最高只支持 2^29 以内的数")

    # 生成测试数据
    limit = 1 << n
    a_real = random.randrange(limit)
    b_real = random.randrange(limit)

    # 以下是对原交互逻辑的无 input() 改写
    # 原协议：打印 "? x y" 后等待一行 '0'/'1' 作为比较结果
    # 这里用 oracle(a_real, b_real, x, y) 直接获得结果

    # 初始比较 "? 0 0"
    ans00 = oracle(a_real, b_real, 0, 0)  # '1' 若 a_real > b_real, 否则 '0'
    xr = 0
    a = 0
    b = 0
    cb = 2 ** 29  # 与原程序保持一致的最高位

    while cb:
        # "? xr + cb  cb" -> ans11
        ans11 = oracle(a_real, b_real, xr + cb, cb)

        # "? xr  cb"
        if ans11 == ans00:
            ans01 = oracle(a_real, b_real, xr, cb)
            if ans01 == '1':
                a += cb
                b += cb
        else:
            ans00 = oracle(a_real, b_real, xr, cb)
            if ans11 == '1':
                b += cb
            else:
                a += cb
            xr += cb

        cb //= 2

    # 模拟输出：原程序是 print("!", a, b)
    # 这里返回推断结果与真实值，便于调用方校验
    return (a, b), (a_real, b_real)


if __name__ == "__main__":
    # 示例：以 n = 10 运行一次
    inferred, real = main(10)
    print("inferred a, b:", inferred)
    print("real     a, b:", real)