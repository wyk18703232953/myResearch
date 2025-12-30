import random

def main(n):
    # 这里的 n 作为测试数量，生成 n 个随机整数进行测试
    # 每个整数的绝对值上界可按需调整，例如 10**9
    test_data = [random.randint(-10**9, 10**9) for _ in range(n)]

    for x in test_data:
        res = transform_number(x)
        print(res)

def transform_number(n):
    if n >= 0:
        return n
    else:
        a = str(n)[1:]  # 去掉负号
        if len(a) > 2:
            # 第一种删除策略：去掉倒数第二位
            a1 = a[::-1][1:][::-1]
            num1 = int(a1)

            # 第二种删除策略：去掉倒数第三位
            a2 = str(n)[1:]
            b = a2[::-1]
            p1 = b[0]
            p2 = b[2:]
            p = (p1 + p2)[::-1]
            num2 = int(p)

            small = min(num1, num2)
            return -small

        elif len(a) == 2:
            m = a[0]
            k = a[1]
            small = min(int(m), int(k))
            return -small

        else:
            # 原程序对 len(a) == 1 的情况未明确处理
            # 按原意：负的一位数只能是该数本身
            return n

if __name__ == "__main__":
    # 示例：生成并处理 5 组测试数据
    main(5)