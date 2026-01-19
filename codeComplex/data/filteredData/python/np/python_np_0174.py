def set(mask, pos):
    return mask | (1 << pos)

def isOn(mask, pos):
    return (mask & (1 << pos)) > 0

def main(n):
    # 对于给定的规模 n，构造确定性的输入：
    # n: 元素个数
    # l, r, x: 根据 n 确定生成，使得约束随规模变化但保持确定性
    # dif: 长度为 n 的整数列表
    if n <= 0:
        print(0)
        return

    # 构造参数 l, r, x，使其随 n 可扩展且确定
    # 这里设置：
    # dif[i] = i + 1
    # l = n
    # r = n * (n + 1) // 2  (所有元素和)
    # x = max(1, n // 3)
    dif = [i + 1 for i in range(n)]
    l = n
    r = n * (n + 1) // 2
    x = n // 3
    if x == 0:
        x = 1

    count = 0
    mask = 0

    # 和原程序保持一致的枚举方式
    while mask <= 2 ** n:
        summ = []
        bit = 0

        while bit < n:
            if isOn(mask, bit):
                summ.append(dif[bit])
            bit += 1

        if summ:
            total = sum(summ)
            if total <= r and total >= l and max(summ) - min(summ) >= x:
                count += 1

        mask += 1

    print(count)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)