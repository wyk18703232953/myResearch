import random

def main(n):
    # 根据规模 n 生成测试数据：lst[0], lst[1]
    # 这里简单设定：lst[0] 在 [1, n]，lst[1] 在 [1, 2n]
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(2, 2 * n))

    lst = [x, y]

    if lst[1] > 2 * lst[0] - 1:
        print(0)
    else:
        if lst[1] % 2 == 1:
            countr = (lst[1] - 1) // 2
        else:
            countr = (lst[1] - 2) // 2
        if lst[1] > lst[0] + 1:
            countr = countr - lst[1] + lst[0] + 1
        print(countr)

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)