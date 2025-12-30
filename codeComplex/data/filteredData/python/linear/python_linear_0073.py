import random

def main(n: int):
    # 生成测试数据：
    # 令 a 的长度为 n，b 的长度为 n + k（k 可自定义，这里取 n//2）
    len_a = n
    len_b = n + n // 2 if n > 0 else 0

    # 随机生成只含 '0' 和 '1' 的字符串 a 和 b
    a = ''.join(random.choice('01') for _ in range(len_a))
    b = ''.join(random.choice('01') for _ in range(len_b))

    ans = 0

    ones = [0 for _ in range(len(b) + 1)]
    zeros = [0 for _ in range(len(b) + 1)]

    for i in range(len(b)):
        ones[i] = ones[i - 1] + int(b[i])
        zeros[i] = i + 1 - ones[i]

    # 注意：当 i == 0 时，zeros[i-1] / ones[i-1] 即 zeros[-1] / ones[-1]，
    # 保持与原程序行为一致
    for i in range(len(a)):
        if a[i] == '1':
            ans += zeros[len(b) - len(a) + i] - zeros[i - 1]
        else:
            ans += ones[len(b) - len(a) + i] - ones[i - 1]

    print(ans)


if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)