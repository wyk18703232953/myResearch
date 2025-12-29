import random

def main(n):
    # 生成测试数据
    # 约束：1 ≤ l ≤ r，x ≥ 0，n ≥ 1
    # 题意：从 n 个数中选出若干个，使得和在 [l, r] 内，且最大值与最小值之差 ≥ x
    # 这里根据 n 生成一个简单合理的测试数据
    c = sorted(random.randint(1, 100) for _ in range(n))
    total_sum = sum(c)

    # 将 l, r 和 x 设为与数据规模相关的值
    l = total_sum // 4
    r = total_sum * 3 // 4
    x = max(1, (max(c) - min(c)) // 3)

    def func():
        count = 0
        for mask in range(1 << n):
            temp = []
            for j in range(n):
                if (1 << j) & mask:
                    temp.append(c[j])

            if not temp:
                continue

            s = sum(temp)
            if l <= s <= r and temp[-1] - temp[0] >= x:
                count += 1
        print(count)

    func()


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)