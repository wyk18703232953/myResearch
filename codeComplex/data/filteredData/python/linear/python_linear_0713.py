def main(n):
    # 确定性生成长度为 n 的数组
    arr = [(i * 3 + 5) for i in range(n)]

    ans = 10 ** 10
    for i in range(n):
        x = i if i > n - i - 1 else n - i - 1
        # 避免除以 0 的情况：当 x 为 0 时跳过该位置
        if x == 0:
            continue
        ans = min(ans, arr[i] // x)

    print(ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行实验
    main(10)