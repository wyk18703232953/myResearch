def main(n):
    text = 'RGB' * 2222
    # 将 n 映射为测试组数 T，以及每组的字符串长度 len_s 和窗口大小 k
    # 保证规模可控且随 n 线性增长
    T = max(1, n // 3)
    len_s = max(3, n)        # 字符串长度
    k = max(1, len_s // 2)   # 窗口大小，保证 1 <= k <= len_s

    answers = []
    for t in range(T):
        # 构造一个确定性的字符串 s（长度为 len_s），模式随 t 变化
        # 使用 (i + t) % 3 在 'R','G','B' 中循环
        s_chars = []
        for i in range(len_s):
            c = 'RGB'[(i + t) % 3]
            s_chars.append(c)
        s = ''.join(s_chars)

        ans = 2222
        for i in range(3):
            p = text[i:k + i]
            for j in range(len_s - k + 1):
                diff = 0
                for l in range(j, j + k):
                    if s[l] != p[l - j]:
                        diff += 1
                if diff < ans:
                    ans = diff
        answers.append(ans)

    # 打印所有测试组结果
    for v in answers:
        # print(v)
        pass
if __name__ == "__main__":
    # 示例调用，可以根据需要修改 n 的大小做实验
    main(10)