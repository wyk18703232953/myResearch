import random

def main(n):
    # 生成测试数据：三个正整数 k1, k2, k3，范围 1~n（至少为 1）
    n = max(1, n)
    k1 = random.randint(1, n)
    k2 = random.randint(1, n)
    k3 = random.randint(1, n)

    a = [k1, k2, k3]
    a = sorted(a)

    dp = [0] * 5001
    dp[0] = 1

    # 第一轮
    i = 0
    while i <= 5000:
        if dp[i] == 0 and i + a[0] <= 5000:
            while i + a[0] <= 5000:
                dp[i] = 1
                i = i + a[0]
        else:
            i += 1

    # 第二轮
    i = 0
    while i <= 5000:
        if dp[i] == 0 and i + a[1] <= 5000:
            while i + a[1] <= 5000:
                dp[i] = 1
                i = i + a[1]
        else:
            i += 1

    # 第三轮
    i = 0
    while i <= 5000:
        if dp[i] == 0 and i + a[2] <= 5000:
            while i + a[2] <= 5000:
                dp[i] = 1
                i = i + a[2]
        else:
            i += 1

    dp = dp[:2002]
    if dp.count(0) == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用：规模参数可自行修改
    main(100)