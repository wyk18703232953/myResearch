import random

def main(n):
    # 生成测试数据
    # 约定：k 为一个正整数模数，nums 为长度为 n 的整数数组
    # 这里示例：k 在 [1, 10^9] 中随机，nums 中每个数在 [1, 10^9] 中随机
    k = random.randint(1, 10**9)
    nums = [random.randint(1, 10**9) for _ in range(n)]

    counts = [{} for _ in range(11)]

    for val in nums:
        a = val
        for i in range(11):
            r = a % k
            try:
                counts[i][r] += 1
            except KeyError:
                counts[i][r] = 1
            a *= 10

    res = 0
    for i in nums:
        wo = str(i)
        le = len(wo)
        mimo = (k - (i % k)) % k
        if mimo in counts[le]:
            res += counts[le][mimo]
            if int(wo + wo) % k == 0:
                res -= 1

    print(res)

# 示例调用
if __name__ == "__main__":
    main(10)