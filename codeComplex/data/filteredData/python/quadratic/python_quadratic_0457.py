import random

def main(n: int):
    # 生成规模为 n 的测试数据：1 <= lister[i] <= n
    a = n
    lister = [random.randint(1, n) for _ in range(a)]

    ans = dict()

    def findans(idx: int) -> bool:
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

    print(''.join(level))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)