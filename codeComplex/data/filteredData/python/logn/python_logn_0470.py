import random

def main(n):
    # 生成两个不超过 n 的非负整数 a 和 b 作为测试数据
    # 为了涵盖完整 30 位范围，n 至少建议为 (1 << 30) - 1
    max_val = min(n, (1 << 30) - 1)
    a = random.randint(0, max_val)
    b = random.randint(0, max_val)

    # 交互函数的模拟：返回 a^b 与传入 x,y 的比较结果（字符串 '0' 或 '1'）
    target = a ^ b

    def query(x, y):
        return '1' if (target ^ x) > (target ^ y) else '0'

    # 原逻辑的主过程，但用 query() 替代输入输出交互
    ans00 = query(0, 0)
    xr = 0
    ra = 0
    rb = 0
    cb = 2 ** 29
    while cb:
        ans11 = query(xr + cb, cb)
        ans10 = query(xr, cb)
        if ans11 == ans00:
            ans01 = ans10
            if ans01 == '1':
                ra += cb
                rb += cb
        else:
            ans00 = ans10
            if ans11 == '1':
                rb += cb
            else:
                ra += cb
            xr += cb
        cb //= 2

    # 输出：原始测试数据和通过算法恢复的结果
    print("original a b:", a, b)
    print("recovered a b:", ra, rb)


if __name__ == "__main__":
    # 示例：n 取 2^30-1
    main((1 << 30) - 1)