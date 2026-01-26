def main(n):
    # 输入结构：一个长度为 4 的整数列表 [n, pos, l, r]
    # 这里复用参数名，原题中的 n 记为 total
    total = max(1, n)  # 保证区间上限至少为 1
    # 构造一个确定性的 (pos, l, r)
    # 让 l,r 在 [1,total] 范围内，且 l <= r
    if total == 1:
        pos = 1
        l = 1
        r = 1

    else:
        pos = (n % total) + 1
        l = (n // 2) % total + 1
        r = (n * 3) % total + 1
        if l > r:
            l, r = r, l

    x = [total, pos, l, r]

    pos = x[1]
    total = x[0]
    l = x[2]
    r = x[3]
    step = 0
    if pos < l:
        step = l - pos + 1
        if r < total:
            step += r - l + 1
    elif pos > r:
        step = pos - r + 1
        if l > 1:
            step += r - l + 1

    else:
        if l > 1 and total > r:
            step += min(pos - l, r - pos) + r - l + 2
        elif l == 1 and total > r:
            step = r - pos + 1
        elif l > 1 and total == r:
            step += pos - l + 1

        else:
            step = 0

    # print(step)
    pass
if __name__ == "__main__":
    # 示例：运行多个不同规模的实验
    for n in [1, 5, 10, 100]:
        main(n)