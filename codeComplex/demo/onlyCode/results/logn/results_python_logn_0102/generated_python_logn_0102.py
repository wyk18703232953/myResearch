def main(n: int):
    # 根据规模 n 生成测试数据，这里简单设定区间 [l, r] = [0, n]
    l, r = 0, n

    if l == r:
        print(0)
    else:
        if (r & (r - 1) == 0):
            print(r ^ (r - 1))
        else:
            x = l ^ r
            p = 1
            while p <= x:
                p *= 2
            print(p - 1)


if __name__ == "__main__":
    # 示例运行，可根据需要修改 n
    main(10)