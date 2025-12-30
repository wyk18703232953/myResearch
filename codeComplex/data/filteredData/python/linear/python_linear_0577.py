from math import log2

def main(n):
    # 生成规模为 n 的测试数据：这里直接以 n 作为逻辑规模参数使用
    if n == 1:
        print(1)
        return
    elif n == 3:
        print(1, 1, 3)
        return

    l = [1] * (n // 2)
    if n % 2 == 1:
        l.append(1)

    xn = int(log2(n))
    tmp = n - len(l)
    for i in range(2, xn + 1):
        fn = tmp // 2
        if tmp % 2 == 1:
            fn += 1
        tmp -= fn
        l += ([pow(2, i - 1)] * fn)

    l.append((n // pow(2, xn - 1)) * pow(2, xn - 1))
    print(' '.join(str(i) for i in l))


if __name__ == "__main__":
    # 示例：调用 main 生成规模为 10 的结果
    main(10)