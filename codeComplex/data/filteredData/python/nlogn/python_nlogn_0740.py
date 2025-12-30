import random

def main(n):
    a = 'cslnb'
    b = 'sjfnb'

    # 根据 n 生成测试数据 ns
    # 这里生成 0 到 2n 范围内的随机整数，可按需修改生成策略
    ns = [random.randint(0, 2 * n) for _ in range(n)]

    ns.sort()
    ans = []

    for i in range(1, n):
        if ns[i] == ns[i - 1]:
            ans.append(i)

    if len(ans) >= 2 or sum(ns) == 0:
        print(a)
        return

    if len(ans) == 1:
        i = ans[0]
        if ns[i] == 0 or (ns[i] - 1) in ns:
            print(a)
            return
        r = sum(ns) - n * (n - 1) // 2
        if r % 2 == 0:
            print(a)
            return
        else:
            print(b)
            return
    else:
        r = sum(ns) - n * (n - 1) // 2
        if r % 2 == 0:
            print(a)
        else:
            print(b)


# 示例调用
if __name__ == "__main__":
    main(5)