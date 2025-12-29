def main(n: int):
    import random
    import string

    # 生成长度为 n 的随机小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    c = set(s)
    ln = [0] * n
    for d in c:
        last = -1
        for i, v in enumerate(s):
            if v == d:
                last = i
            if last == -1:
                ln[i] = int(1e9)
            else:
                ln[i] = max(ln[i], i - last + 1)
    print(min(ln))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)