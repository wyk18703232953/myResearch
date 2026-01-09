def main(n):
    # n 表示整数 a 的位数
    # 构造确定性的 a 和 b
    if n <= 0:
        # print(0)
        pass
        return

    # 构造一个有 n 位的整数 a：从 1~9 循环填充
    digits = [(i % 9) + 1 for i in range(n)]
    a_val = int(''.join(str(d) for d in digits))

    # 构造上界 b：略大于 a 的一个确定性值
    # 这里令 b = a_val * 2
    b_val = a_val * 2

    # 以下为原逻辑，只是用生成的 a_val, b_val
    a = list(str(a_val))
    a.sort()
    ans = []
    while a:
        for i in range(len(a) - 1, -1, -1):
            c = ans + [a[i]] + a[:i] + a[i+1:]
            if int(''.join(c)) <= b_val:
                ans.append(a[i])
                a.pop(i)
                break
    # print(''.join(ans))
    pass
if __name__ == "__main__":
    main(10)