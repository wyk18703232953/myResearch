def main(n: int):
    # 根据 n 生成测试数据，这里将原来固定的 2229 / 2228
    # 与 n 线性关联，保证可以随规模变化
    len1 = n
    len2 = max(1, n - 1)

    # 原程序逻辑：第一行全是 '4'，第二行是若干个 '5' 加一个 '6'
    line1 = '4' * len1
    line2 = '5' * len2 + '6'

    print(line1)
    print(line2)


if __name__ == "__main__":
    # 这里可修改为任意需要的规模 n
    main(2229)