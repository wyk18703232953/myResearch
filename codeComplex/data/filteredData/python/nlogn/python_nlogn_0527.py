import random

def main(n):
    # 生成测试数据：k 和长度为 n 的数组 a
    # 可根据需要调整数据范围
    k = random.randint(1, 10**9) or 1  # 确保 k 不为 0
    a = [random.randint(1, 10**9) for _ in range(n)]

    a_pows = []
    a_pow_dict = [{} for _ in range(11)]
    for j in range(n):
        x = a[j] % k
        i = 0
        while i < 11:
            if x in a_pow_dict[i]:
                a_pow_dict[i][x] += 1
            else:
                a_pow_dict[i][x] = 1
            i += 1
            x = (x * 10) % k

    c = 0

    for x in a:
        m = len(str(x))
        if (-x) % k in a_pow_dict[m]:
            c += a_pow_dict[m][(-x) % k]
            c -= int(int(str(x) * 2) % k == 0)

    print(c)
    return c

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)