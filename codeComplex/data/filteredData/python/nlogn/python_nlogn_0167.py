def main(n: int):
    # 根据 n 生成测试数据：
    # 这里示例生成 n 个点 p 和半径 w，使得 p = i, w = i % 3
    # 你可以根据需求修改数据生成方式
    endpoints = []
    for i in range(n):
        p = i
        w = i % 3
        endpoints.append([p - w, p + w])

    # 按右端点排序
    endpoints.sort(key=lambda sublist: sublist[1])

    res = 0
    bottom = 10**18 * -1

    for pt in range(len(endpoints)):
        if endpoints[pt][0] >= bottom:
            res += 1
            bottom = endpoints[pt][1]

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改或在外部调用 main
    main(10)