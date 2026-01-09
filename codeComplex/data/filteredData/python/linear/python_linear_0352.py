def main(n):
    # 将 n 映射为原程序中的 n 和 m
    # 这里设定 m = n，生成 n 条 (x, y) 输入对
    m = n

    # 确定性生成 m 组 (x, y)，不影响后续逻辑，但保留结构
    pairs = [(i, (i * 2) % (n + 1 if n > 0 else 1)) for i in range(m)]

    cnt = 0
    ans = []
    for i in range(n):
        if cnt % 2 == 0:
            ans.append("0")

        else:
            ans.append("1")
        cnt += 1

    result = "".join(ans)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)