def main(n):
    # n 控制输入规模：数组长度 a = n，元素为确定性构造
    a = n if n > 0 else 1
    lister = [(i % a) + 1 for i in range(a)]

    ans = {}

    def findans(idx):
        if idx in ans:
            return ans[idx]
        mod = idx % lister[idx]
        ok = True
        if idx + lister[idx] >= a and idx - lister[idx] < 0:
            ok = False

        else:
            for i in range(mod, a, lister[idx]):
                if i != idx and lister[i] > lister[idx]:
                    ok = ok and findans(i)
            ok = not ok
        ans[idx] = ok
        return ok

    for i in range(len(lister)):
        findans(i)

    level = []
    for i in range(a):
        if ans[i]:
            level.append('A')

        else:
            level.append('B')

    # print(''.join(level))
    pass
if __name__ == "__main__":
    main(10)