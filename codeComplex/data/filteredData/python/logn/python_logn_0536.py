def main(n: int):
    # 生成测试数据：这里直接使用传入的 n 作为原程序中的 k
    k = n

    a = [9]
    i = 1
    if k < 10:
        # print(k)
        pass

    else:
        while k > a[-1]:
            a.append((10 ** (i + 1) - 10 ** i) * (i + 1) + a[i - 1])
            i += 1

        cat = len(a)
        diff = k - a[-2]
        step = int(diff / cat)
        rem = diff % cat

        if rem == 0:
            number = (10 ** (cat - 1) - 1) + step
            # print(str(number)[-1])
            pass

        else:
            number = 10 ** (cat - 1) + step
            # print(str(number)[rem - 1])
            pass
if __name__ == "__main__":
    # 示例：可在此修改 n 以进行不同规模的测试
    main(1000)