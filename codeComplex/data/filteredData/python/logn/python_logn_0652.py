import random

def main(n: int):
    # 生成测试数据：
    # 原程序读取 x = [x[0], x[1]]
    # x[0] 作为搜索上界+1；x[1] 作为 target。
    # 为了保证存在解，这里构造一个满足条件的 (x[0], x[1])。
    #
    # 逻辑回顾：
    # 给定 n0 = x[0]，在区间 [0, n0-1] 中二分 mid，
    # sum = mid*(mid+1)//2
    # ans1 = n0 - mid
    # 条件：sum - ans1 == target
    #
    # 构造策略：
    # 任取 n0, mid，使 mid 在 [0, n0-1]，然后令 target = sum - ans1。

    # 令 n 决定 n0 的规模
    n0 = max(2, n)  # 至少为2，避免过小
    mid = random.randint(0, n0 - 1)
    sum_mid = mid * (mid + 1) // 2
    ans1_true = n0 - mid
    target = sum_mid - ans1_true

    x = [n0, target]

    # 以下为原逻辑封装
    start = 0
    end = x[0] - 1
    target = x[1]
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        sum_mid = mid * (mid + 1) // 2
        ans1 = x[0] - mid

        if sum_mid - ans1 == target:
            ans = ans1
            break
        elif sum_mid - ans1 > target:
            end = mid - 1
        else:
            start = mid + 1

    print(ans)


if __name__ == "__main__":
    # 示例：n 可以根据需要修改
    main(10)