def main(n):
    # 解释输入结构：原程序读入 n, k 以及一个长度为 n 的数组 p
    # 这里将参数 n 视为数组 p 的长度，同时从 n 中确定性构造 k 和 p

    if n <= 0:
        return

    # 确定性地构造 k，使得 1 <= k <= 10 且随 n 可变化
    k = max(1, (n % 10) + 1)

    # 确定性地构造长度为 n 的数组 p，元素在 [0, 255] 范围内
    # 使用一个简单的算术序列并取模 256
    p = [((i * 17 + 31) % 256) for i in range(n)]

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

    # print(" ".join(map(str, p)))
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的规模进行实验
    main(1000)