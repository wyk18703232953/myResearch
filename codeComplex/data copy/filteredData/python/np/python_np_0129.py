import math

M = mod = 10 ** 9 + 7

def factors(n):
    return sorted(set(
        sum(([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0), [])
    ))

def inv_mod(n):
    return pow(n, mod - 2, mod)

def main(n):
    # 生成确定性输入：
    # n: 数组长度
    # l[i] = i + 2  (避免出现 0 和 1，全为正整数)
    # c[i] = (i % 7) + 1  (正权重，有限周期)
    if n <= 0:
        print(-1)
        return

    l = [i + 2 for i in range(n)]
    c = [(i % 7) + 1 for i in range(n)]

    element = l[0]
    for i in range(1, n):
        element = math.gcd(element, l[i])

    if element != 1:
        print(-1)
        return

    myset = {}

    for ind, val in enumerate(l):
        # 遍历当前已有的 gcd 状态
        for j in list(myset):
            temp = math.gcd(j, val)
            cost = myset[j] + c[ind]
            if temp not in myset:
                myset[temp] = cost
            else:
                if cost < myset[temp]:
                    myset[temp] = cost

        # 单独使用当前元素
        if val not in myset:
            myset[val] = c[ind]
        else:
            if c[ind] < myset[val]:
                myset[val] = c[ind]

    print(myset[1])

if __name__ == "__main__":
    # 示例：以 n = 10 作为规模运行
    main(10)