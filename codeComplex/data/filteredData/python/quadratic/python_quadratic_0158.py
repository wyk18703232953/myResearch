import random

def main(n):
    # 生成测试数据：n 和 k，随后生成长度为 n 的数组 p（元素在 [0, 255]）
    # 这里示例设定：1 <= n <= 256，1 <= k <= 256
    n = max(1, min(256, int(n)))
    k = random.randint(1, 256)
    p = [random.randint(0, 255) for _ in range(n)]

    choosed = [False] * 256
    left = [i for i in range(256)]

    for i, x in enumerate(p):
        if not choosed[x]:
            best = x
            for j in range(x - 1, max(-1, x - k), -1):
                if not choosed[j]:
                    best = j
                else:
                    if x - left[j] < k:
                        best = left[j]
                    break
            for j in range(best, x + 1):
                choosed[j] = True
                left[j] = best
        p[i] = left[x]

    print(' '.join(map(str, p)))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)