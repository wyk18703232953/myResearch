import random

def main(n):
    # 生成测试数据：n 和数组 A（长度为 n，元素为 1~10*n 的随机整数）
    m = n  # 原代码中读入了 m，但实际并未使用，这里保持形式
    A = [random.randint(1, 10 * n) for _ in range(n)]

    if n == 1:
        print(0)
        return

    A.sort(reverse=True)

    NOW = A[0]
    ANS = 1
    i = 1
    while i < n:
        if A[i] == A[i - 1]:
            NOW = max(1, NOW - 1)
            ANS += 1
        else:
            if A[i] >= NOW - 1:
                ANS += 1
                NOW = max(NOW - 1, 1)
            else:
                ANS += max(1, NOW - A[i])
                NOW = A[i]
        i += 1

    ANS += (NOW - 1)
    print(sum(A) - ANS)


if __name__ == "__main__":
    # 示例运行
    main(10)