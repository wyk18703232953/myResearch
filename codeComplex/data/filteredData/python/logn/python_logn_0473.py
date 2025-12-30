import random

def main(n):
    """
    n: 比特位规模（原代码是 0..29 共 30 位，这里用 n 控制）
    内部随机生成两个整数 A, B（0 <= A, B < 2^n），
    模拟交互，最后打印还原出的 a, b 以及真实的 A, B，便于验证。
    """
    # 生成测试数据：隐藏的 A, B
    A = random.randint(0, (1 << n) - 1)
    B = random.randint(0, (1 << n) - 1)

    # 定义交互：比较 (x ^ A) 与 (y ^ B)
    # 返回字符串 "1" 当 (x ^ A) > (y ^ B)
    # 返回字符串 "-1" 当 (x ^ A) < (y ^ B)
    # 返回字符串 "0" 当相等（理论上不会触发原逻辑中的第三种分支）
    def query(x, y):
        v1 = x ^ A
        v2 = y ^ B
        if v1 > v2:
            return "1"
        elif v1 < v2:
            return "-1"
        else:
            return "0"

    # 对应原程序：先问 "? 0 0"
    res = query(0, 0)
    a = 0
    b = 0

    # 按位从高到低恢复 a, b
    for i in range(n - 1, -1, -1):
        res1 = query(a ^ (1 << i), b)
        res2 = query(a, b ^ (1 << i))
        if res1 == res2:
            if res == "1":
                a ^= 1 << i
            else:
                b ^= 1 << i
            res = res1
        elif res1 == "-1":
            a ^= 1 << i
            b ^= 1 << i
        else:
            # res1 == "1" 的情况，原交互题中此分支不会进入
            # 保留以防模拟中遇到；这里不修改 a, b
            pass

    # 输出推测的 a, b 以及真实 A, B，便于测试和验证
    print("deduced a =", a, "b =", b)
    print("real    A =", A, "B =", B)
    print("correct:", a == A and b == B)


if __name__ == "__main__":
    # 示例：n = 30 与原代码一致
    main(30)