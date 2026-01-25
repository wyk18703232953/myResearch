def main(n):
    # 生成长度为 n 的只含 '+' 和 '-' 的字符串 s
    # i 为偶数时为 '+'，奇数时为 '-'
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    t = 0
    for ch in s:
        if ch == '+':
            t += 1
        else:
            t = max(t - 1, 0)

    result = max(t, 0)
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)