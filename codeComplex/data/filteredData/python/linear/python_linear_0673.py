def main(n):
    a = [(i * 3 + 1) % 7 for i in range(n)]
    b = []
    for i in range(n):
        a[i] %= 2
        if len(b) != 0:
            if b[-1] == a[i]:
                b.pop()

            else:
                b.append(a[i])

        else:
            b.append(a[i])
    if len(b) > 1:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(10)