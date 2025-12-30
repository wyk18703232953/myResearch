def main(n):
    # 1. 生成测试数据：长度为 n 的 0/1 序列
    #    你可以按需要修改生成逻辑，例如全 1、随机等
    # 这里用简单的模式：前半段 1，后半段 0
    if n <= 0:
        return
    half = n // 2
    ls = [1 if i < half else 0 for i in range(n)]

    # 2. 计算前缀和数组 pre
    pre = []
    s = 0
    for v in ls:
        s += v
        pre.append(s)

    # 3. 原始逻辑：判断是否存在划分
    for i in range(n - 1):
        cnt = 0
        su = 0
        for j in range(i + 1, n):
            su += ls[j]
            if su == pre[i]:
                cnt += 1
                su = 0
        if cnt and su == 0:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)