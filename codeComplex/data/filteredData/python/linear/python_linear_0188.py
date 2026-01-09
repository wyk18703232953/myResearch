import bisect

def main(n):
    # 生成长度为 n 的数组 a，元素为 1, 2, ..., n
    a = [i + 1 for i in range(n)]
    p = [0]
    for x in a:
        p.append(p[-1] + x)
    result = bisect.bisect_left(p, p[-1] / 2)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)