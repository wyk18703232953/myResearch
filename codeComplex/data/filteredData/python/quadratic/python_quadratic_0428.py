def main(n):
    # 生成确定性输入：长度为 n 的数字字符串，循环使用 1..9
    if n <= 0:
        return "NO"
    s = "".join(str((i % 9) + 1) for i in range(n))

    a = []
    for v in s:
        if v != '0' and v != '\n':
            a.append(v)
    if not a and n > 1:
        return 'YES'
    n_local = len(a)
    s_local = a
    total = 0
    for i in range(n_local - 1):
        total += int(s_local[i])
        j = i + 1
        check = 1
        while j < n_local:
            temp = int(s_local[j])
            j += 1
            while j < n_local:
                if temp >= total:
                    break
                temp += int(s_local[j])
                j += 1
            if total != temp:
                check = 1
                break
        if total != temp:
            check = 0
        if check:
            return 'YES'
    return 'NO'


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    print(main(10))