import random

def main(n):
    for _ in range(n):
        # 生成测试数据：两个正整数 a, b（可根据需要调整范围）
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)

        if a > b or a == b:
            c, d = a, b
        else:
            c, d = b, a

        e = [0]

        def fun(c, d):
            e[0] += c // d
            f = d
            d = c % d
            c = f
            if f > 0 and d > 0:
                fun(c, d)

        fun(c, d)
        print(e[0])


if __name__ == "__main__":
    # 示例：运行规模 n = 5
    main(5)