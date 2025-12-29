import math
import random

def countDigit(n):
    return math.floor(math.log(n, 10) + 1)


def solve(n):
    count = countDigit(n)
    if count == 1:
        return n
    else:
        low = 1
        high = 9
        prefix_sum = [0, 9]
        digit = 0

        for i in range(2, 16):
            low *= 10
            high = high * 10 + 9
            prefix_sum.append((high - low + 1) * i + prefix_sum[i - 1])

            if n < prefix_sum[i]:
                digit = i
                break

        x = n - prefix_sum[digit - 1]
        q = x // digit
        r = x % digit
        low = int(math.pow(10, digit - 1))
        low = low + q - 1

        if r == 0:
            return low % 10
        else:
            num = low + 1
            stringnum = str(num)
            return int(stringnum[r - 1])


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设规模 n 表示要生成的查询次数，
    # 每次查询的位置在 [1, 10^15] 范围内。
    max_pos = 10 ** 15
    results = []
    for _ in range(n):
        pos = random.randint(1, max_pos)
        results.append((pos, solve(pos)))

    # 输出：每行 “位置 结果”
    for pos, ans in results:
        print(pos, ans)


if __name__ == "__main__":
    # 示例：规模 5
    main(5)