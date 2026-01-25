def main(n):
    if n <= 0:
        print(0)
        print(-1, -1)
        return

    # 生成确定性的字符串 s 和 t，长度为 n，字母表为前 26 个小写字母
    # s[i] = chr(97 + (i % 26))
    # t[i] = chr(97 + ((i + 1) % 26)) 使得大部分位置不同，便于时间复杂度实验
    s = [chr(97 + (i % 26)) for i in range(n)]
    t = [chr(97 + ((i + 1) % 26)) for i in range(n)]

    d = {}
    ans = 0
    x, y = -1, -1
    for i in range(n):
        if s[i] != t[i]:
            d[(s[i], t[i])] = i
            ans += 1
    l = [chr(i + 97) for i in range(26)]
    for i in l:
        for j in l:
            if (i, j) in d and (j, i) in d:
                ans -= 2
                x = d[(i, j)] + 1
                y = d[(j, i)] + 1
                break
        if x != -1:
            break
    if x == -1 and y == -1:
        for i in l:
            for j in l:
                for k in l:
                    if (i, j) in d and (j, k) in d:
                        ans -= 1
                        x = d[(i, j)] + 1
                        y = d[(j, k)] + 1
                        break
                if x != -1:
                    break
            if x != -1:
                break
    print(ans)
    print(x, y)


if __name__ == "__main__":
    main(1000)