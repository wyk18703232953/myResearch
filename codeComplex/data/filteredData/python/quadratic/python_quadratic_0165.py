def main(n):
    # 这里根据 n 生成一组测试数据 (n, k, p)
    # 你可以按需要修改生成逻辑
    k = max(1, n // 3)  # 示例：令 k 与 n 相关
    p = list(range(n))  # 示例：p 为 0,1,2,...,n-1

    mp = {}  # 不要覆写内建 map
    res = []

    for pi in p:
        if mp.get(pi) is None:
            key = pi
            for j in range(pi, pi - k, -1):
                if j < 0:
                    break
                if mp.get(j) is None:
                    key = j

                else:
                    if mp[j] >= pi - k + 1:
                        key = mp[j]
                    break
            for j in range(pi, key - 1, -1):
                if mp.get(j):
                    break
                mp[j] = key
        res.append(mp[pi])

    # print(*res, sep=" ")
    pass
if __name__ == "__main__":
    # 示例调用
    main(10)