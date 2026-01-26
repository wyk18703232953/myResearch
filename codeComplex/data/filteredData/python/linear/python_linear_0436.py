def main(n):
    m = int(n ** 0.5)
    if m == 0:
        # print()
        pass
        return
    a = []
    for i in range(0, n, m):
        for j in range(i, min(i + m, n)):
            a.append(min(i + m, n) - j + i)
    # print(' '.join(str(x) for x in a))
    pass
if __name__ == "__main__":
    main(1000)