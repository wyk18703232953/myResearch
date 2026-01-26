def main(n):
    from collections import defaultdict as dd

    # 数据生成：生成 n 个区间 [l, r]
    # 使得：
    #   l = i
    #   r = i + (i % 5)
    # 这样保证确定性且规模随 n 增长
    d = dd(int)
    for i in range(1, n + 1):
        l = i
        r = i + (i % 5)
        d[l] += 1
        d[r + 1] -= 1

    arr = list(d.keys())
    arr.sort()
    ans = [0 for _ in range(n + 1)]
    count = 0
    l_arr = len(arr)
    arr.append(arr[-1])
    for i in range(l_arr):
        count += d[arr[i]]
        if 0 <= count <= n:
            ans[count] += arr[i + 1] - arr[i]

    # 原程序输出 ans[1:]
    # print(*ans[1:])
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小进行时间复杂度实验
    main(10)