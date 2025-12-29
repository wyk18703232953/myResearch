import random

def main(n):
    # 生成测试数据：a, b 为 [0, n) 内随机整数
    # 并模拟交互环境，所有 input() 替换为对 compare 函数的调用
    max_val = n
    a = random.randrange(max_val)
    b = random.randrange(max_val)

    # 被比较的“黑盒”函数，对应原题中的交互判定逻辑
    # 根据原程序的使用方式，可以推断：
    #   print("? x y") 后 input() 读到的是 f(x, y) = (a ^ x) > (b ^ y) ? '1' : '0'
    # 其中 ^ 为按位异或
    def query(x, y):
        return '1' if (a ^ x) > (b ^ y) else '0'

    # 下方是对原程序的改写：用 query() 替代 input()
    xr = 0
    A = 0
    B = 0

    # cb 最大应覆盖到 n 的最高位；若 n 为 0，直接退出
    if max_val == 0:
        print("!", A, B)
        return

    # 取不小于 n 的最高二次幂
    cb = 1
    while cb <= max_val:
        cb <<= 1
    cb >>= 1  # 最高有效位

    ans00 = query(0, 0)

    while cb:
        ans11 = query(xr + cb, cb)
        ans_xr_cb = query(xr, cb)

        if ans11 == ans00:
            ans01 = ans_xr_cb
            if ans01 == '1':
                A += cb
                B += cb
        else:
            ans00 = ans_xr_cb
            if ans11 == '1':
                B += cb
            else:
                A += cb
            xr += cb

        cb //= 2

    # 输出推断出的 a, b 与真实的 a, b 以验证正确性
    print("real a b:", a, b)
    print("calc a b:", A, B)


# 示例运行
if __name__ == "__main__":
    # 例如 n=2**30，可以覆盖原代码的位数范围
    main(1 << 30)