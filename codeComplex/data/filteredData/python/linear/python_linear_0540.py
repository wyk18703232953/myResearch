def main(n):
    # 确定性生成输入数组 a，长度为 n
    # 采用简单的算术构造，既包含正数也包含负数和零（当 n 足够大时）
    a = []
    for i in range(n):
        # 生成模式: 交替正负，并周期性产生 0
        # 例如: n=5 -> [0, 2, -3, 4, -5]
        val = (i + 1)
        if i % 5 == 0:
            val = 0
        elif i % 2 == 0:
            val = -val
        a.append(val)

    if n == 0:
        # 原题没有 n=0 情况，这里约定输出 0
        # print(0)
        pass
        return

    if n == 1:
        # print(a[0])
        pass

    else:
        sm = 0
        havePositive = False
        haveNegative = False

        for c in a:
            if c == 0:
                haveNegative = True
                havePositive = True
            elif c > 0:
                havePositive = True
                sm += c

            else:
                haveNegative = True
                sm -= c

        if haveNegative and havePositive:
            # print(sm)
            pass

        else:
            for i in range(n):
                a[i] = abs(a[i])
            ans = sum(a)
            low = a[0]
            for c in a:
                low = min(low, c)
            # print(ans - 2 * low)
            pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 的规模进行复杂度实验
    main(10)