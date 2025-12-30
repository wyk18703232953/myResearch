from collections import defaultdict
import random

def main(n: int):
    # 生成测试数据：n 个随机整数，范围可根据需要调整
    # 为了让程序更容易找到满足条件的三元组，使用较小范围
    a = [random.randint(-10**6, 10**6) for _ in range(n)]

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

    print(mxSiz)
    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main，n 可自行调整
    main(10)