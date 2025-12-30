from math import ceil, log
import random

def main(n):
    # 1. 生成规模为 n 的测试数据：随机正整数数组
    #    这里假设数值范围为 1 ~ 10^6，可按需要自行调整
    a = [random.randint(1, 10**6) for _ in range(n)]

    # 2. 原逻辑开始
    d = {}
    m = -1
    mm = 10**10

    for v in a:
        d[v] = d.get(v, 0) + 1
        if v > m:
            m = v
        if v < mm:
            mm = v

    ans = 0

    for v in a:
        exponent = ceil(log(v, 2))
        power = 2 ** exponent
        find = 0
        while power - v >= 0:
            if power - v > mm and power - v > m:
                break

            element = power - v
            if element in d and element == v and d[element] > 1:
                find = 1
                break
            elif element in d and element != v:
                find = 1
                break

            power = power * 2

        if find == 0:
            ans += 1

    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)