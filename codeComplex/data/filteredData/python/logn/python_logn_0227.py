def main(n):
    # 根据 n 生成测试数据，这里简单设定 s 为 n 的一半（也可按需修改）
    s = n // 2

    num = ''
    div = 9

    if s // 10 != 0:
        div = 9
        while (s // div) // 10 != 0:
            div = div * 10 + 9
        while div:
            rem = str(s // div)
            if int(rem) > 9:
                num = str(int(num) + 1) + '0' * len(str(div))
                div = 0
                s = 0
                break
            else:
                num += rem
            s = s % div
            div //= 10
        num += str(s)
    else:
        num = str(s)

    mini = int(num)
    if mini % 10 != 0:
        mini += 10
        mini -= mini % 10

    print(max(0, n - mini + 1))


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)