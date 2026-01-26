def main(n):
    # 将 n 映射到输入规模：构造一组确定性的 (x, y, z, t1, t2, t3)
    # 这里 n 只是用来生成数据，不影响算法逻辑本身
    x = n
    y = n // 2
    z = n % 10
    t1 = (n % 5) + 1          # 保证 t1 >= 1
    t2 = ((n // 3) % 5) + 1   # 保证 t2 >= 1
    t3 = ((n // 7) % 5) + 1   # 保证 t3 >= 1

    if abs(z - x) * t2 + 3 * t3 + abs(x - y) * t2 <= abs(x - y) * t1:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)