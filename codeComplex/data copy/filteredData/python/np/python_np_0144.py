def main(n):
    # 生成测试数据：将 m 设为 1..(2^(n-1)) 的中间值，保证合法
    if n <= 1:
        m = 1

    else:
        m = 1 << (n - 2)  # 取中间值作为示例

    v = [0] * 51
    left = 1
    right = n
    for i in range(1, n + 1):
        if n - i - 1 <= 0:
            pw = 1

        else:
            pw = 1 << (n - i - 1)

        if m <= pw:
            v[left] = i
            left += 1

        else:
            v[right] = i
            right -= 1
            m -= pw

    # 输出结果
    if n >= 1:
        for i in range(1, n):
            # print(v[i], end=' ')
            pass
        # print(v[n])
        pass
if __name__ == "__main__":
    # 示例调用：可自行修改 n 的值
    main(5)