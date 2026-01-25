from collections import Counter

def main(n):
    # n 表示数组 a 的长度
    # 确定性生成：a[i] = (i * 2 + i // 2) % (n // 2 + 1 if n // 2 + 1 > 0 else 1)
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        # 原题中至少会有一个数，这里约定 n=0 时直接返回
        return

    a = [(i * 2 + i // 2) % (n // 2 + 1 if n // 2 + 1 > 0 else 1) for i in range(n)]

    d = dict()
    z = 0
    s = 0
    for item in a:
        if item in d:
            d[item] += 1
            z = item
        else:
            d[item] = 1
        s += item

    if len(a) - len(d) >= 2:
        print("cslnb")
        return

    if len(a) == len(d):
        z = (n * (n - 1)) // 2
        if (s - z) % 2:
            print("sjfnb")
        else:
            print("cslnb")
    else:
        if z - 1 in d or z == 0:
            print("cslnb")
        else:
            zz = (n * (n - 1)) // 2
            if (s - zz) % 2:
                print("sjfnb")
            else:
                print("cslnb")


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的大小
    main(10)