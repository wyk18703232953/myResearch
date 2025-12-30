def solve_range_xor_diff(l: int, r: int) -> int:
    if l == r:
        return 0
    a = bin(l)[2:]
    b = bin(r)[2:]
    x = len(a)
    y = len(b)
    if x != y:
        ans = 0
        for i in range(y):
            ans += (2 ** i)
        return ans
    else:
        for i in range(x):
            if a[i] != b[i]:
                ind = i
                break
        length = x - ind
        ans = 0
        for i in range(length):
            ans += (2 ** i)
        return ans


def main(n: int):
    # 生成测试数据：构造一对 (l, r)，满足 0 <= l <= r
    # 这里示例生成：l = n，r = 2*n + 1（可根据需要自行修改）
    l = n
    r = 2 * n + 1

    ans = solve_range_xor_diff(l, r)
    print(ans)


if __name__ == "__main__":
    # 示例：可在此处手动调用 main 进行简单测试
    # 实际使用时，由调用方直接调用 main(n)
    main(5)