import random

def main(n):
    # 生成测试数据：长度为 n 的由 '0' 和 '1' 组成的字符串
    a = [random.choice(['0', '1']) for _ in range(n)]
    b = [random.choice(['0', '1']) for _ in range(n)]

    ans = 0

    for i in range(n - 1):
        if a[i] == b[i]:
            continue
        if a[i + 1] == b[i + 1]:
            continue

        if a[i] == b[i + 1] and a[i + 1] == b[i]:
            a[i], a[i + 1] = a[i + 1], a[i]
            ans += 1

    for i in range(n):
        ans += a[i] != b[i]

    print(ans)


if __name__ == "__main__":
    # 示例：n=10，可按需修改
    main(10)