def main(n):
    # 生成确定性输入：长度为 n 的整数列表 t
    # 这里使用简单的算术构造：t[i] = (i % 5) + 1，保证所有元素为正整数
    t = [(i % 5) + 1 for i in range(n)]

    p = sum(t)
    import math
    a = math.ceil(p / 2)

    u = 0
    for j in range(n):
        u += t[j]
        if u >= a:
            # print(j + 1)
            pass
            break


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小
    main(10)