def main(n):
    # n 表示数组长度
    k = 3
    l = [i * 2 + (i % 3) for i in range(1, n + 1)]
    l = sorted(l)

    res = set()
    for i in l:
        if i % k != 0 or i // k not in res:
            res.add(i)

    return len(res)


if __name__ == "__main__":
    print(main(10))