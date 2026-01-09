def main(n):
    if n <= 0:
        return

    # 确定性生成长度为 n 的列表 t
    # 示例构造：t[i] = (i % 5) + 1，元素取值在 1~5 之间
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
    main(10)