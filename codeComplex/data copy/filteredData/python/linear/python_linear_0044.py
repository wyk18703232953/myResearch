def main(n):
    # 规模含义：
    # n 表示数组 a 的长度
    # k 取 min(5, n)（至少为 1）
    if n <= 0:
        # print(-1, -1)
        pass
        return

    k = min(5, n)
    # 构造一个确定性的整数数组 a，元素值有规律重复
    # 保证既有重复，又有不同值，便于算法运行
    a = [(i * 2 + 3) % (n // 2 + 3) for i in range(n)]

    q = {0}
    e = 0
    l = []
    for i in range(n):
        if a[i] not in q:
            e += 1
            q.add(a[i])
        if e == k:
            e = 0
            q = {0}
            l += [i]

    w = 10 ** 5
    t = 0
    for i in l:
        e = 0
        q = {0}
        for j in range(i, -1, -1):
            if a[j] not in q:
                e += 1
                q.add(a[j])
            if e == k:
                if w > len(q):
                    w = j + 1
                    t = i + 1
                break

    if len(set(a)) >= k:
        # print(w, t)
        pass

    else:
        # print(-1, -1)
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行时间复杂度实验
    main(10)