def main(n):
    a = [i % 5 for i in range(n)]
    b = 0
    for i in range(n):
        if a[i] % 2 == 1:
            if i % 2 == 0:
                b += 1

            else:
                b -= 1
    if n % 2 == 0:
        if b == 0:
            # print("YES")
            pass

        else:
            # print("NO")
            pass

    else:
        if b == 0 or b == 1:
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)