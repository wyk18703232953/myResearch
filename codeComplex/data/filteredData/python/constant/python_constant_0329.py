import random

def main(n):
    # 生成测试数据：长度固定为 14 的数组 a
    # 这里按题意保持 14 个坑位，只用 n 控制数值规模
    random.seed(0)
    a = [random.randint(0, n) for _ in range(14)]

    ans = 0
    for i in range(len(a)):
        x = a[i]
        b = [j for j in a]
        b[i] = 0
        for j in range(len(a)):
            b[j] += x // 14

        for j in range(1, x % 14 + 1):
            b[(i + j) % 14] += 1

        ans_now = 0
        for j in b:
            if j % 2 == 0:
                ans_now += j
        ans = max(ans_now, ans)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 控制生成数据的数值规模
    main(100)