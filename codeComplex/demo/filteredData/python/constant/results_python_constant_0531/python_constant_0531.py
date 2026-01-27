def main(n):
    # 将 n 映射为 (x, y, z, t1, t2, t3)
    # 使得各参数随 n 规模线性或简单变化，且完全确定
    x = n
    y = n // 2
    z = n // 3
    t1 = (n % 7) + 1
    t2 = (n % 5) + 1
    t3 = (n % 3) + 1

    if 3 * t3 + t2 * (abs(z - x) + abs(x - y)) <= t1 * abs(x - y):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)