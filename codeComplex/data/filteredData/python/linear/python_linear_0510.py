def main(n):
    if n <= 0:
        return 0
    a = "".join("A" if i % 2 == 0 else "B" for i in range(n))
    b = "".join("A" if (i + 1) % 2 == 0 else "B" for i in range(n))

    c = [10 ** 10 for _ in range(n + 10)]
    c[0] = 0 if a[0] == b[0] else 1

    for i in range(1, n):
        if a[i] == b[i]:
            c[i] = c[i - 1]
        elif a[i] == b[i - 1] and a[i - 1] == b[i]:
            c[i] = (1 + c[i - 2] if i > 1 else 1)
        c[i] = min(c[i], c[i - 1] + 1)

    return c[n - 1]


if __name__ == "__main__":
    # 示例调用
    for size in [1, 2, 5, 10]:
        # print(size, main(size))
        pass