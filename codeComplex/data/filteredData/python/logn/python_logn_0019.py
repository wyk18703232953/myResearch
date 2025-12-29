import random

def main(n: int):
    """
    n 作为生成测试数据的规模上限：
    随机生成 0 <= l <= r <= n 的一组数据并执行原逻辑。
    """
    # 生成测试数据：0 <= l <= r <= n
    l = random.randint(0, n)
    r = random.randint(l, n)

    if l == r:
        print(0)
        return

    binr, binl = list(bin(r)[2:]), list(bin(l)[2:])
    binl = ['0'] * (len(binr) - len(binl)) + binl

    for i in range(len(binl)):
        if binl[i] != binr[i]:
            binl = '1' * (len(binl[i:]))
            break

    print(int(binl, 2))


if __name__ == "__main__":
    # 示例：规模上限 n = 10**6，可按需修改
    main(10**6)