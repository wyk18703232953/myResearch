import random

def main(n: int):
    # 生成两个 n 位非负整数 a_true, b_true 作为测试数据
    # 范围控制在 [0, 2^n - 1]
    max_val = (1 << n) - 1
    a_true = random.randint(0, max_val)
    b_true = random.randint(0, max_val)

    # 定义“交互裁判”：给定 (x, y) 返回符号比较结果
    # 原交互中返回 '1' / '0' / '-1'，这里做一个合理假设：
    # - 返回 '1'  : if (a_true ^ x) > (b_true ^ y)
    # - 返回 '0'  : if (a_true ^ x) < (b_true ^ y)
    # - 返回 '-1' : if (a_true ^ x) == (b_true ^ y)
    def judge(x, y):
        v1 = a_true ^ x
        v2 = b_true ^ y
        if v1 > v2:
            return '1'
        elif v1 < v2:
            return '0'
        else:
            return '-1'

    # 以下是将原始交互式程序改写为调用 judge 的形式
    # 原代码：
    # print("? 0 0"); res = input()
    res = judge(0, 0)
    a = 0
    b = 0
    # 原程序从 29 降到 0，这里使用 n-1 降到 0
    for i in range(n - 1, -1, -1):
        # print("?", (a^(1<<i)), b); res1 = input()
        res1 = judge(a ^ (1 << i), b)
        # print("?", a, (b^(1<<i))); res2 = input()
        res2 = judge(a, b ^ (1 << i))

        if res1 == res2:
            if res == '1':
                a ^= (1 << i)
            else:
                b ^= (1 << i)
            res = res1
        elif res1 == '-1':
            a ^= (1 << i)
            b ^= (1 << i)

    # 输出推测得到的 a, b 以及真实的 a_true, b_true 以便验证
    print("guessed:", a, b)
    print("actual: ", a_true, b_true)
    print("correct:", a == a_true and b == b_true)


if __name__ == "__main__":
    # 示例：n=30 时与原程序等价（原程序固定 0..29 共 30 位）
    main(30)