def main(n):
    import random

    # 生成测试数据：随机选择 k，范围 [1, 2^n - 1]（确保有足够比特位）
    # 若想和原题更贴近，可设 k 在 [0, 2^(n-1)] 或 [1, n] 之类，根据需要修改
    if n <= 1:
        # 原代码在 for i in range(n-2, -1, -1) 中，当 n<=1 时循环为空
        # 直接输出 n 本身即可
        print(n)
        return

    # 为避免超大整数，这里将 k 限制在 [1, 2^(n-1) - 1]
    max_k = (1 << (n - 1)) - 1
    if max_k <= 0:
        k = 0
    else:
        k = random.randint(1, max_k)

    pre, post = [], []
    k -= 1
    v = 1
    for i in range(n - 2, -1, -1):
        if k & (1 << i):
            post.append(v)
        else:
            pre.append(v)
        v += 1
    print(*pre, n, *reversed(post))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)