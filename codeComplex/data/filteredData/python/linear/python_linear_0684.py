import random

def main(n):
    # 1. 生成测试数据 b，长度为 n
    # 为了能构造出合法的 a，这里先随机构造 a，再生成符合题意的 b
    # 原逻辑: 给定 b，构造 a
    # 这里反向：先随机构造 a，再计算 b[i] = a[i] + a[-i-1]
    if n <= 0:
        return

    # 随机构造 a，长度为 2n
    # 为避免负数，使用非负随机数
    a = [random.randint(0, 10) for _ in range(2 * n)]

    # 根据 a 构造 b
    b = [a[i] + a[-i-1] for i in range(n)]

    # 2. 将原逻辑封装为函数，根据 b 求 a2
    a2 = [0] * (2 * len(b))
    a2[-1] = b[0]
    for i in range(1, len(b)):
        if b[i] - a2[i - 1] <= a2[-i]:
            a2[i] = a2[i - 1]
            a2[-i - 1] = b[i] - a2[i - 1]
        else:
            a2[-i - 1] = a2[-i]
            a2[i] = b[i] - a2[-i - 1]

    # 3. 输出结果（模拟原程序输出）
    print(*a2)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)