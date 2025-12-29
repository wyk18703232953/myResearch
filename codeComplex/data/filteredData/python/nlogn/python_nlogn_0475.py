import copy
import random


def main(n: int):
    # 1. 根据规模 n 生成测试数据
    # 这里假设 m 为“每个桶的最大容量”的上界，随 n 增长
    # 也可以根据需求自行调整生成策略
    m = max(1, n // 2)

    # 生成 n 个正整数，范围 [1, m]
    arr = [random.randint(1, m) for _ in range(n)]

    # 2. 将原逻辑封装到 main 中
    res = [0] * (max(arr) + 1)
    for x in arr:
        res[x] += 1

    ans = 0
    for d in range(1, m + 1):
        temp = copy.deepcopy(res)
        cnt = 0
        for i in range(len(temp)):
            while temp[i] >= d:
                temp[i] -= d
                cnt += 1
        if cnt >= n:
            ans = max(ans, d)

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)