import sys

def main(n):
    if n < 3:
        # print(-1)
        pass
        return

    # 确定性生成 l 和 c，长度为 n
    # l: 严格正整数，带一些重复和递增结构
    l = [1 + (i * 2) % (n + 3) for i in range(n)]
    # c: 成本值，正整数，构造方式与 l 不同以打乱关联
    c = [1 + (i * 3 + 2) % (2 * n + 5) for i in range(n)]

    a = []
    for i in range(1, n - 1):
        lr = sys.maxsize
        lc = sys.maxsize
        for j in range(0, i):
            if l[i] > l[j]:
                if c[j] < lc:
                    lc = c[j]
        for j in range(i + 1, n):
            if l[j] > l[i]:
                if c[j] < lr:
                    lr = c[j]
        if lr < sys.maxsize and lc < sys.maxsize:
            a.append(lr + lc + c[i])
    if not a:
        # print(-1)
        pass

    else:
        # print(min(a))
        pass
if __name__ == "__main__":
    main(10)