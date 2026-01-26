def main(n):
    # 生成确定性的测试数据：长度为 n 的整数列表
    # 这里采用简单的算术构造：e = i % (max(1, n // 3))
    if n <= 0:
        return
    k = max(1, n // 3)
    E = [i % k for i in range(n)]

    D = {}
    for e in E:
        D[e] = D.get(e, 0) + 1
    for e in E:
        # print(D[e])
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小
    main(10)