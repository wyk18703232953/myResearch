def main(n):
    # 根据规模 n 生成 s（测试数据示例：取一半）
    s = n // 2

    if s >= n:
        print('0')
    else:
        for i in range(s, n + 2):
            l = 0
            for j in str(i):
                l += int(j)
            if i - l >= s:
                break
        print(n - i + 1)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(1000)