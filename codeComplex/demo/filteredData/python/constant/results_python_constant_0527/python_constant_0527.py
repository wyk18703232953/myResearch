def main(n):
    # 生成确定性输入数据
    # 将 n 映射为 x, y, z, t1, t2, t3
    x = n
    y = n // 2
    z = (n * 3) // 4
    t1 = (n % 5) + 1
    t2 = (n % 7) + 1
    t3 = (n % 11) + 1

    if abs(x - y) * t1 >= abs(x - z) * t2 + t3 * 3 + abs(x - y) * t2:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)