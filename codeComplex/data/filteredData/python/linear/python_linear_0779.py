def main(n):
    a = [(i * 2) % (n // 2 + 1) for i in range(n)]  # 确定性生成长度为 n 的整数序列
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
        # print("cslnb")
        pass
        return
    if len(a) == len(d):
        z = (n * (n - 1)) // 2
        if (s - z) % 2:
            # print("sjfnb")
            pass

        else:
            # print("cslnb")
            pass

    else:
        if z - 1 in d or z == 0:
            # print("cslnb")
            pass

        else:
            zz = (n * (n - 1)) // 2
            if (s - zz) % 2:
                # print("sjfnb")
                pass

            else:
                # print("cslnb")
                pass
if __name__ == "__main__":
    main(10)