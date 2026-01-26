def main(n):
    # 映射含义：
    # n: 数组 v 的长度
    # 固定 k，与 n 解耦，使规模仅由 n 控制
    k = max(1, n // 2)

    # 生成确定性数组 v，大小为 n
    # 元素分布可覆盖不同相对大小关系：递增序列带有周期性偏移
    v = [(i * 3) % (2 * n + 1) for i in range(n)]

    v.sort()
    cnt = 0
    ar = [0] * (n + 5)
    for i in range(len(v)):
        while cnt > 0 and v[i] > ar[cnt] and v[i] <= k + ar[cnt]:
            cnt -= 1
        cnt += 1
        ar[cnt] = v[i]
    # print(cnt)
    pass
if __name__ == "__main__":
    main(10)