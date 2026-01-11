import sys

def main(n):
    # 映射规则：给定 n，构造 (n, k)
    # 这里选择 k = max(1, n // 2)，保证规模随 n 线性增长
    if n <= 0:
        return
    k = max(1, n // 2)

    total = n * k
    ans = []
    for i in range(1, total + 1):
        if i % 2:
            x, y = divmod(i // 2, k)
            ans.append((x + 1, y + 1))

        else:
            x, y = divmod(total - i // 2, k)
            ans.append((x + 1, y + 1))

    out_lines = ["{} {}".format(x, y) for x, y in ans]
    # sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次调用
    main(10)