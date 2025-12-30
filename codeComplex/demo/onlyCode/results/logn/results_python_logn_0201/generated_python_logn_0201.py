import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里令 s 在 [1, n] 区间内随机取值
    s = random.randint(1, n)

    sol = 0
    l = 1
    r = n
    while l <= r:
        digit_sum = 0
        i = (l + r) // 2
        a = i
        while a > 0:
            digit_sum += a % 10
            a //= 10

        if i - digit_sum >= s:
            sol = n - i + 1
            r = i - 1
        else:
            l = i + 1

    print(sol)


if __name__ == "__main__":
    # 示例：可自行修改 n 的规模
    main(10**6)