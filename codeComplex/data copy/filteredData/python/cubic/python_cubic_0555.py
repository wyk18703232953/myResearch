def main(n):
    a_str = "".join(str((i % 10)) for i in range(1, n + 1)) or "0"
    b = int("".join(str(((i * 7) % 10)) for i in range(1, n + 1)) or "0")

    a = sorted(a_str, reverse=True)
    k = ""
    while len(a) > 0:
        for i in range(len(a)):
            num = k + a[i] + "".join(sorted(a[:i] + a[i + 1:]))
            if int(num) <= b:
                k += a[i]
                a = a[:i] + a[i + 1:]
                break
    # print(k)
    pass
if __name__ == "__main__":
    main(5)