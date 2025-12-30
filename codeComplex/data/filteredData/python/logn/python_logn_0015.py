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
    # 使得 1 <= a <= b <= 2^n - 1
    if n <= 0:
        return

    max_val = (1 << n) - 1
    # 简单构造：a 为 2^(n-1)，b 为 2^n - 1
    a = 1 << (n - 1)
    b = max_val

    print(f(a, b))


if __name__ == "__main__":
    # 示例：可以在这里调用 main，规模自行调整
    main(5)