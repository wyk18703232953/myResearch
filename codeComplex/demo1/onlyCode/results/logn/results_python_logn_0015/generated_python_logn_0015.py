def f(a, b):
    r = list(bin(b).lstrip("0b"))
    l = list((len(bin(b)) - len(bin(a))) * ("0") + bin(a).lstrip("0b"))
    for i in range(len(r)):
        if r[i] == "1" and l[i] == "1":
            r[i] = "0"
            if int("".join(r), 2) >= a:
                pass
            else:
                r[i] = "1"
        if l[i] == "0" and r[i] == "0":
            l[i] = "1"
            if int("".join(l), 2) <= b:
                pass
            else:
                l[i] = "0"
    l = int("".join(l), 2)
    r = int("".join(r), 2)
    return l ^ r


def main(n):
    # 根据规模 n 生成测试数据：
    # 让 b 约为 2^n，a 为 [2^(n-1), 2^n - 1] 范围内的某个数
    if n <= 0:
        a, b = 1, 1
    else:
        b = (1 << n) - 1          # 最大 n 位二进制数
        a = (1 << (n - 1))        # 最小 n 位二进制数的一半规模

    # 调用原逻辑
    result = f(a, b)
    print(result)


if __name__ == "__main__":
    # 示例：使用规模 n=5 运行
    main(5)