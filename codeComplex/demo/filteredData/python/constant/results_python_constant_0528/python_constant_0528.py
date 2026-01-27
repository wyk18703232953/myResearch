def main(n):
    # 映射 n 到输入规模：使用 n 生成一组确定性参数 (x, y, z, t1, t2, t3)
    # 保证随 n 变化，数值整体规模线性增长，便于时间复杂度实验
    x = n
    y = n // 2
    z = (n * 3) // 4
    t1 = (n % 5) + 1
    t2 = (n % 7) + 1
    t3 = (n % 3) + 1

    elevator = t2 * (abs(x - y) + abs(z - x)) + 3 * t3
    stairs = t1 * abs(x - y)

    if elevator > stairs:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
if __name__ == "__main__":
    main(10)