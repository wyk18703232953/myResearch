def main(n):
    # n controls both the size of c and the value of b in a deterministic way
    if n <= 0:
        n = 1

    a = n
    b = (n % 26) + 1

    abc = "abcdefghijklmnopqrstuvwxyz"
    # deterministically construct c: repeating pattern of abc up to length n
    c = "".join(abc[i % 26] for i in range(n))

    summa = 0
    count = 0
    j = -2
    i = 0
    while i < 26 and count < b:
        if abc[i] in c and i - 2 >= j:
            summa += i + 1
            count += 1
            j = i
        i += 1

    if count < b:
        print(-1)
    else:
        print(summa)


if __name__ == "__main__":
    main(10)