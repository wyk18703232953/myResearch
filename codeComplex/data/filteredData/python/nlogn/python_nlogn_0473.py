import copy
import random


def main(n):
    # 生成测试数据
    # 设定值域上限和总和规模（可根据需要调整）
    m = max(1, n * 2)              # d 的最大可能值
    max_val = max(1, n * 3)        # arr 中元素的最大值
    arr = [random.randint(1, max_val) for _ in range(n)]

    # 原逻辑
    res = [0] * (max(arr) + 1)
    for i in arr:
        res[i] += 1

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
    # 示例：规模为 10
    main(10)