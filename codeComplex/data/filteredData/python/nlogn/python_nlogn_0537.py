from collections import defaultdict
import random


class Digit:
    def __init__(self):
        self.count = defaultdict(int)

    def increment(self, k):
        self.count[k] += 1

    def found(self, k):
        return self.count.get(k, 0)


def main(n):
    # 根据 n 生成测试数据：
    # 约定：mod 为一个合理的正整数，array 为长度为 n 的随机整数数组
    # 可根据需要修改生成规则
    if n <= 0:
        print(0)
        return

    mod = 10**9 + 7  # 示例：取大质数作为模
    # 生成 n 个随机正整数，范围可根据需求调整
    array = [random.randint(1, 10**9) for _ in range(n)]

    ans = 0
    digits = [Digit() for _ in range(11)]

    # 第一部分：预处理
    for i in range(n):
        temp = array[i] % mod
        for j in range(10):
            temp = (temp * 10) % mod
            digits[j + 1].increment(temp)

    # 第二部分：统计匹配数量
    for i in range(n):
        temp = array[i]
        count = 0
        while temp > 0:
            temp //= 10
            count += 1

        find = (mod - array[i] % mod) % mod
        ans += digits[count].found(find)

    # 第三部分：排除自身组合
    for i in range(n):
        temp1 = array[i] % mod
        temp2 = array[i]

        while temp2 > 0:
            temp2 //= 10
            temp1 = (temp1 * 10) % mod

        if (temp1 + array[i]) % mod == 0:
            ans -= 1

    print(ans)


if __name__ == "__main__":
    # 示例调用：n=5
    main(5)