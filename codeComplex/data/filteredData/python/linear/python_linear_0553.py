def main(n):
    a = [i % (n // 2 + 1) for i in range(n)]
    s = 0
    for j, i in enumerate(a):
        if i > s:
            # print(j + 1)
            pass
            return
        if i == s:
            s += 1
    # print(-1)
    pass
if __name__ == "__main__":
    main(10)