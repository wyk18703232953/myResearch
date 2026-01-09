def main(n):
    # 这里的 n 表示字符串长度
    # 构造一个确定性的数字串，例如循环使用 0..9
    s = "".join(str(i % 10) for i in range(n))
    # 为避免全部为 '0' 导致 trivial 情况，可在开头放一个非零
    if n > 0:
        s = "1" + s[1:] if n > 1 else "1"

    num = int(s)
    list_n = list(s)
    list_n_int = list(map(int, s))

    lower = max(list_n_int)
    total = sum(list_n_int)
    upper = int(total / 2)

    flag = False
    if lower == 0:
        # print("YES")
        pass

    else:
        for i in range(lower, upper + 1):
            flag = True
            p = 0
            temp = 0
            each = i
            seg = total / each
            if seg.is_integer():
                while p < len(s):
                    temp += list_n_int[p]
                    if temp < each:
                        p += 1
                    elif temp == each:
                        temp = 0
                        p += 1

                    else:
                        flag = False
                        break
                if flag:
                    # print("YES")
                    pass
                    break

            else:
                flag = False
        if not flag:
            # print("NO")
            pass
if __name__ == "__main__":
    # 示例：n 为字符串长度，可根据实验需求调整
    main(20)