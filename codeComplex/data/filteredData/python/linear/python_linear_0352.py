def main(n):
    # 映射：给定 n，构造 m = n，生成 n 条边 (x, y)，但不影响核心逻辑
    m = n
    edges = []
    for i in range(m):
        x = i % n if n > 0 else 0
        y = (i + 1) % n if n > 0 else 0
        edges.append((x, y))

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