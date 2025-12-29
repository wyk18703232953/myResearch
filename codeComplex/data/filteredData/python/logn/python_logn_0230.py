import random

def bigNumber(n, s):
    for i in range(s, n + 1):
        sumVal = 0
        num = i
        while num:
            sumVal += num % 10
            num //= 10
        if i - sumVal >= s:
            print(n - i + 1)
            return
    print(0)

def main(n):
    # 根据规模 n 生成测试数据
    # 约定：1 <= s <= n
    s = random.randint(1, n)
    bigNumber(n, s)

# 示例调用
# main(100000)