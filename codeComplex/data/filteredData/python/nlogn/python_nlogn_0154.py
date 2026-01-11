def main(n):
    # 映射：n 作为数组长度，k 为一个与 n 有关的确定性整数
    k = max(2, n // 3 + 1)
    l = [(i * 2 + 3) % (5 * k + 7) + 1 for i in range(n)]

    p = []
    a = sorted(l)
    for i in a:
        if i % k == 0:
            if i // k in p:
                pass

            else:
                p.append(i)

        else:
            p.append(i)
    result = len(set(p))
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)