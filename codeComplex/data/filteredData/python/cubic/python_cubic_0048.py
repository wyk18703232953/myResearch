def main(n):
    # 生成长度为 n 的确定性字符串
    # 这里使用周期性字母序列，保证当 n > 26 时一定存在重复子串
    if n <= 0:
        # print(0)
        pass
        return

    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    n_len = len(s)
    for L in range(n_len - 1, 0, -1):
        if len({s[i:i + L] for i in range(n_len - L + 1)}) < n_len - L + 1:
            # print(L)
            pass
            break

    else:
        # print(0)
        pass
if __name__ == "__main__":
    # 示例：使用规模 n = 100 进行一次运行
    main(100)