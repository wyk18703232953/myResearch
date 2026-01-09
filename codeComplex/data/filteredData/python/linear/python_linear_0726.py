def main(n):
    # 示例：根据 n 生成一个合适的 k
    # 这里简单设定 k = n // 3，且确保 0 <= k < n
    k = n // 3
    if k >= n:
        k = max(0, n - 1)

    d = (n - k) // 2 + 1
    ans = ['1' if (i + 1) % d == 0 else '0' for i in range(n)]
    result = ''.join(ans)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)