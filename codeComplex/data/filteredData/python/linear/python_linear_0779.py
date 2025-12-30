import random

def main(n):
    # 生成测试数据：长度为 n 的非负整数数组 a
    # 为了保证规模合理，数值范围设置为 [0, n]
    a = [random.randint(0, n) for _ in range(n)]

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
    # 示例：运行规模 n = 10
    main(10)