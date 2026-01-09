def main(n):
    # 解释输入结构：
    # 原程序输入：x y z t1 t2 t3
    # 我们让 n 作为位置 x，其他值由 n 确定性构造
    x = n
    y = n // 2
    z = (2 * n) // 3
    t1 = (n % 5) + 1
    t2 = (n % 7) + 1
    t3 = (n % 3) + 1

    a = abs(x - y) * t1
    b = abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3
    if b <= a:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)