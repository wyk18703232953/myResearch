def main(n):
    from collections import defaultdict

    dct = defaultdict(int)
    lst = [0.0] * n

    # 生成确定性的输入字符串列表，形式类似 "(a+b)/c"
    # a, b, c 通过简单算术构造，确保完全确定
    for i in range(n):
        a = i
        b = i % 7 + 1       # 避免太简单的重复模式
        c = (i % 5) + 1     # 保证 c >= 1，避免除零
        expr = f"({a}+{b})/{c}"

        t = expr.strip()
        plus_idx = t.index('+')
        right_paren_idx = t.index(')')
        slash_idx = t.index('/')

        a_val = int(t[1:plus_idx])
        b_val = int(t[plus_idx + 1:right_paren_idx])
        c_val = int(t[slash_idx + 1:])

        x = (a_val + b_val) / c_val
        lst[i] = x
        dct[x] += 1

    for i in lst:
        # print(dct[i], end=' ')
        pass
if __name__ == "__main__":
    main(10)