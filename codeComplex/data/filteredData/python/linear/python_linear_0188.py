import bisect

def main(n):
    # 生成确定性输入数据：长度为 n 的整数序列
    # a[i] = (i % 5) + 1，确保所有元素为正，前缀和严格递增
    a = [(i % 5) + 1 for i in range(n)]
    p = [0]
    for x in a:
        p.append(p[-1] + x)
    ans = bisect.bisect_left(p, p[-1] / 2)
    print(ans)
    return ans

if __name__ == "__main__":
    main(10)