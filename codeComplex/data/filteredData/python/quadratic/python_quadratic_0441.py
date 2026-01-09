def main(n):
    # n 表示数字串长度
    if n <= 0:
        # print("NO")
        pass
        return

    # 确定性生成长度为 n 的数字串 a
    # 使用简单周期模式 1..9 重复
    digits = [(i % 9) + 1 for i in range(n)]
    a = "".join(str(d) for d in digits)

    total_sum = 0
    for x in a:
        total_sum += int(x)
    ans = "NO"
    if total_sum == 0:
        ans = "YES"
    s = 1
    while s * s <= total_sum and ans == "NO":
        if total_sum % s == 0:
            t = 0
            flag = 0
            for x in a:
                t += int(x)
                if t == s:
                    flag = 1
                if t > s:
                    if flag == 1:
                        flag = 0
                        t = int(x)
                        if t == s:
                            flag = 1
            if t == s and t != total_sum:
                ans = "YES"
            t = 0
            flag = 0
            part = total_sum // s
            for x in a:
                t += int(x)
                if t == part:
                    flag = 1
                if t > part:
                    if flag == 1:
                        flag = 0
                        t = int(x)
                        if t == part:
                            flag = 1
            if t == part and t != total_sum:
                ans = "YES"
        s += 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：输入规模为 10
    main(10)