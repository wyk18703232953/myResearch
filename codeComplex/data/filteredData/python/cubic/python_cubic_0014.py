def main(n):
    # 生成确定性字符串：周期性使用小写字母
    a = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    n_len = len(a)
    for i in range(n_len - 1, -1, -1):
        b = sorted([a[j:j + i] for j in range(n_len - i + 1)])
        if True in [b[j] == b[j - 1] for j in range(1, n_len - i + 1)]:
            # print(i)
            pass
            break

if __name__ == "__main__":
    main(1000)