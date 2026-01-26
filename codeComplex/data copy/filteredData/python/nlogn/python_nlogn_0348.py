def main(n):
    from collections import defaultdict

    # 生成确定性输入数组 a，规模为 n
    # 这里使用简单的算术构造：a[i] = i % 50 - 25，保证有重复和正负数
    a = [i % 50 - 25 for i in range(n)] if n > 0 else [0]

    pow2 = [1 << i for i in range(32)]
    mp = defaultdict(int)
    for x in a:
        mp[x] = 1
    mxSiz = 1
    ans = [a[0]]
    for x in a:
        for y in pow2:
            if x - y in mp and x + y in mp:
                mxSiz = 3
                ans = [x - y, x, x + y]
            if x - y in mp and 2 > mxSiz:
                mxSiz = 2
                ans = [x - y, x]

    # print(mxSiz)
    pass
    # print(*ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行时间复杂度实验
    main(100000)