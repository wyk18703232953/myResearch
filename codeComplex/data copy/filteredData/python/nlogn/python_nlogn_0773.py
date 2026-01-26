def main(n):
    # 生成确定性输入数组 a，长度为 n
    # 例如：a[i] = (i * 7) % (n + 3) + i // 2，保证随 n 变化有一定复杂度
    a = [(i * 7) % (n + 3) + i // 2 for i in range(n)]

    idx = list(range(n))
    idx.sort(key=lambda i: a[i], reverse=True)
    imin = imax = idx[0]
    for i in idx[1:]:
        if i == imin - 1 or i == imax + 1:
            imin = min(imin, i)
            imax = max(imax, i)

        else:
            # print('NO')
            pass
            return
    # print('YES')
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行规模化实验
    main(10)