def main(n):
    # 生成确定性字符串，长度为 n
    # 使用简单周期性模式
    base = "abcd"
    s = "".join(base[i % len(base)] for i in range(n))
    size = len(s)

    ans_got = 0
    for length in range(1, size)[::-1]:
        seen = {}
        for i in range(0, size - length + 1):
            sub = s[i : i + length]
            if sub in seen:
                # print(length)
                pass
                ans_got = 1
                break

            else:
                seen[sub] = 1
        if ans_got == 1:
            break
    if ans_got == 0:
        # print(0)
        pass
if __name__ == "__main__":
    main(1000)