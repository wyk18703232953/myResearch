import itertools

def main(n):
    # 映射：n 即原程序中的 n（题目数量）
    # 其余参数和数据由 n 确定性生成
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # 生成题目难度数组 c，长度为 n，确定性构造
    c = [i * 2 + 1 for i in range(n)]

    counter = 0
    for val in ("".join(seq) for seq in itertools.product("01", repeat=n)):
        if val.count('1') < 2:
            continue
        dif = 0
        mx = float("-inf")
        mn = float("inf")
        for i, bit in enumerate(val):
            if bit == '1':
                dif += c[i]
                mx = max(c[i], mx)
                mn = min(c[i], mn)
        if l <= dif <= r and mx - mn >= x:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main(5)