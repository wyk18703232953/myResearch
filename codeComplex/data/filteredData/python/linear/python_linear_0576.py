def main(n):
    a = [0] * n

    def fun(m, ptr1):
        if m == 1:
            a[ptr1] = 1
        elif m == 2:
            a[ptr1] = 1
            ptr1 += 1
            a[ptr1] = 2
        elif m == 3:
            a[ptr1] = 1
            ptr1 += 1
            a[ptr1] = 1
            ptr1 += 1
            a[ptr1] = 3
        else:
            itera = m - m // 2
            for _ in range(itera):
                a[ptr1] = 1
                ptr1 += 1
            fun(m // 2, ptr1)
            for _ in range(m // 2):
                a[ptr1] = 2 * a[ptr1]
                ptr1 += 1

    if n > 0:
        fun(n, 0)
    for v in a:
        print(v, end=" ")
    print()


if __name__ == "__main__":
    main(10)