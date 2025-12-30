import random

def main(n):
    # 1. 生成测试数据
    # 约束：保证存在至少一个元素等于 m，以匹配原算法中 p.index(0) 的逻辑
    m = random.randint(1, n)          # 目标值
    a = [random.randint(1, n) for _ in range(n)]
    pos = random.randrange(n)
    a[pos] = m                        # 保证至少一个等于 m

    # 2. 按原代码逻辑构造 p 数组
    def intCompare(x):
        if x == m:
            return 0
        if x < m:
            return -1
        return 1

    p = list(map(intCompare, a))

    # 3. 原主逻辑
    ret = 0
    ind = p.index(0)
    tem = 0
    MAXN = 400001
    ret0 = [0] * MAXN
    ret1 = [0] * MAXN
    set0 = set()

    offset = 200000  # 将可能的负下标平移到非负，防止越界

    # 从中间向左统计
    tem = 0
    for i in range(ind, -1, -1):
        tem += p[i]
        ret0[tem + offset] += 1
        set0.add(tem)

    # 从中间向右统计
    tem = 0
    for i in range(ind, n):
        tem += p[i]
        ret1[tem + offset] += 1

    # 统计答案
    for s in set0:
        ret += ret0[s + offset] * (
            ret1[-s + offset] + ret1[1 - s + offset]
        )

    print(ret)


if __name__ == "__main__":
    # 示例调用：可按需修改规模 n
    main(10)