def main(n):
    from math import sqrt

    # 生成长度为 n 的数字列表 l（每个元素为 0~9 的整数）
    # 完全确定性：l[i] = (i * 7 + 3) % 10
    l = [(i * 7 + 3) % 10 for i in range(n)]

    divisors = []
    total = sum(l)
    for j in range(2, int(sqrt(total)) + 1):
        if total % j == 0:
            divisors.extend([j, total // j])

    if total == 0:
        # print("YES")
        pass
        return
    if total != 1:
        divisors.append(1)

    for x in divisors:
        search = x
        index = 0
        summ = 0
        while index < n:
            summ += l[index]
            if summ > search:
                break
            elif summ == search:
                summ = 0
            index += 1
        if summ == 0 and index == n:
            # print("YES")
            pass
            return
    # print("NO")
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)