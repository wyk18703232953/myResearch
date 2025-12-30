import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 layne
    # 这里示例生成范围在 [0, 10*n] 的随机整数
    layne = [random.randint(0, 10 * n) for _ in range(n)]

    mx = max(layne)
    dorf = mx * 2 * n
    indx = 1
    for i in range(n):
        dor = (layne[i] // n) * n
        if (layne[i] % n) - i > 0:
            dor = dor + n + i + 1
        else:
            dor = dor + i + 1
        if dor < dorf:
            dorf = dor
            indx = i + 1
    print(indx)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)