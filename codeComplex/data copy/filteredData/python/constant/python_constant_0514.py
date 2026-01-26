def main(n):
    # 根据 n 确定性生成输入规模
    x = n
    y = -n
    z = n // 2
    t1 = (n % 5) + 1
    t2 = (n % 7) + 1
    t3 = (n % 3) + 1

    if 3 * t3 + abs(x - z) * t2 + abs(x - y) * t2 <= abs(x - y) * t1:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)