def main(n):
    # n 表示字符串长度
    if n <= 0:
        return

    # 构造确定性的 s 和 t
    # 使用周期性的字母序列来保证多重字符情况
    letters = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = letters[:]                    # s 为原序
    t = letters[::-1]                 # t 为 s 的反转，确保 sorted(s) == sorted(t)

    if sorted(s) != sorted(t):
        print(-1)
        return
    else:
        lst = [0] * n
        for i in range(n):
            for j in range(n):
                if s[j] == t[i]:
                    lst[j] = i + 1
                    s[j] = "."
                    break
        ans = 0
        a = []
        for i in range(n):
            for j in range(n - 1):
                if i != j:
                    if lst[j] > lst[j + 1]:
                        ans += 1
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                        a.append(j + 1)
        print(ans)
        if a:
            print(*a)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    main(5)