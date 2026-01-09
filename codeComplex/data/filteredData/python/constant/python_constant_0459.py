def main(n):
    # 映射：n 控制坐标规模，构造三个点 (a,b), (b1,b2), (c1,c2)
    # 原逻辑只依赖相对位置，因此用确定性算式生成
    a = n
    b = n // 2

    # 保证生成的点与原点 (a,b) 不重合，且形式多样
    b1 = a + (n % 5 + 1)
    b2 = b + (n % 7 + 2)

    c1 = a + (n % 3 + 2)
    # 为了触发不同分支，使用一个与 b2 有确定性差异的构造
    c2 = b + ((n // 2) % 5 + 1)

    # 原算法
    b1 -= a
    b2 -= b
    c1 -= a
    c2 -= b
    if b1 == 0 or b2 == 0 or c1 == 0 or c2 == 0:
        # print('NO')
        pass

    else:
        if b1 * c1 < 0 or b2 * c2 <= 0:
            # print('NO')
            pass

        else:
            # print('YES')
            pass
if __name__ == "__main__":
    main(10)