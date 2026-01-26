def main(n):
    if n > 0:
        # print(n)
        pass

    else:
        l = list(str(n))
        last = l[0:len(l) - 1]
        second = l[0:len(l) - 2]
        second += l[-1]
        lR = "".join(last)
        sR = "".join(second)
        # print(max(eval(lR), eval(sR)))
        pass
if __name__ == "__main__":
    # 示例：使用 n = -123456 作为规模参数
    main(-123456)