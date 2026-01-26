def main(n):
    r = []
    for i in range(n):
        # 确定性生成 a, b, c, d
        a = i
        b = i + 1
        c = (i * 2) % (n + 1)
        d = (i * 3) // (n + 1)
        r.append(a + b + c + d)

    thomas = r[0]
    rank = sorted(r, reverse=True).index(thomas) + 1
    # print(rank)
    pass
if __name__ == "__main__":
    main(10)