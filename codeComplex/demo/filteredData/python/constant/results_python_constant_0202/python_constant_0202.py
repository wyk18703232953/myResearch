def main(n):
    # 生成三个整数作为输入规模：
    # k1 = n, k2 = 2n, k3 = 3n（并排序以匹配原程序行为）
    k1, k2, k3 = sorted((n, 2 * n, 3 * n))

    if (
        k1 == 1
        or (k1 == 2 and k2 == 2)
        or (k1 == 3 and k2 == 3 and k3 == 3)
        or (k1 == 2 and k2 == 4 and k3 == 4)
    ):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以进行规模实验
    main(10)