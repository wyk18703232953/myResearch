def main(n):
    # 生成确定性的输入字符串 n_str，长度为 n
    # 使用 0~9 的循环序列，避免全 0 的退化情况
    if n <= 0:
        # 和原程序行为保持一致：不存在输入数字时，可以定义为 "NO"
        print("NO")
        return

    digits = [str(i % 10) for i in range(1, n + 1)]
    n_str = "".join(digits)

    num = int(n_str)
    list_n = list(n_str)
    list_n_int = list(map(int, n_str))

    lower = max(list_n_int)
    total = sum(list_n_int)
    upper = int(total / 2)

    flag = False
    if lower == 0:
        print("YES")
    else:
        for i in range(lower, upper + 1):
            flag = True
            p = 0
            temp = 0
            each = i
            seg = total / each
            if seg.is_integer():
                while p < len(n_str):
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
                    print("YES")
                    break
            else:
                flag = False
        if not flag:
            print("NO")


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做实验
    main(10)