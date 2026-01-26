def main(n):
    # 原程序逻辑：处理一个整数输入 n
    x = n

    if x >= 0:
        # print(x)
        pass
        return

    else:
        s = str(abs(x))
        n1 = int(s[:len(s) - 1])

        temp = s[len(s) - 1]

        n2_prefix = s[:len(s) - 2]
        if n2_prefix == "":
            n2 = int(temp)

        else:
            n2 = int(n2_prefix + temp)

    if n1 <= n2:
        if n1 != 0:
            # print('-' + str(n1))
            pass

        else:
            # print(0)
            pass

    else:
        if n2 != 0:
            # print('-' + str(n2))
            pass

        else:
            # print(0)
            pass
if __name__ == "__main__":
    # 示例调用：使用 n 作为“输入规模”的同时也是原算法的输入
    # 可以根据需要修改为任意确定性的整数
    main(-123456)