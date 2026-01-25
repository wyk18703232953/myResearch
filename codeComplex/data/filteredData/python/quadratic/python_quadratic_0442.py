def main(n):
    # n 表示数组长度，构造一个确定性的数组
    # 使用简单的算术构造：a[i] = (i % 5) + 1
    arr = [(i % 5) + 1 for i in range(n)]

    okk = 0
    s = 0
    for i in range(n - 1):
        s += arr[i]
        cnt = 0
        ok = 1
        sss = 0
        for j in range(i + 1, n):
            cnt += arr[j]
            if cnt == s:
                cnt = 0
                sss += 1
            if cnt > s:
                ok = 0
        if cnt == 0 and sss:
            okk = 1
            break
    print("YES" if okk else "NO")


if __name__ == "__main__":
    # 示例调用，可按需修改 n 来做规模实验
    main(10)