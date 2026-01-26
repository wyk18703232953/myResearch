def main():
    a = sorted(input(), reverse=True)
    b = int(input())
    k = ""
    while len(a) > 0:
        for i in range(len(a)):
            num = k + a[i] + "".join(sorted(a[:i] + a[i + 1:]))
            if int(num) <= b:
                k += a[i]
                a = a[:i] + a[i + 1:]
                break
    print(k)


if __name__ == "__main__":
    main()
