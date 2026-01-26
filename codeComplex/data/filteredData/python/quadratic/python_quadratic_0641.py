def main(n):
    # Generate deterministic input data of size n
    # Example: a[i] = i + 1, list length = n
    a = [i + 1 for i in range(n)]

    a.sort()
    count = 0
    for i in range(n):
        cur_c = a[i]
        if not cur_c:
            continue
        count += 1
        for j in range(i + 1, n):
            if a[j] % cur_c == 0:
                a[j] = 0
    # print(count)
    pass
if __name__ == "__main__":
    main(10)