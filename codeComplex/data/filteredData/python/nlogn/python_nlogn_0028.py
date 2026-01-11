def main(n):
    # Generate deterministic input data of size n
    # Original input: first line n (unused except length), second line: list of n integers as strings
    # Here we make a list with some repetitions to keep the "set" behavior meaningful
    l1 = []
    for i in range(n):
        # deterministic integer pattern with repetitions
        val = (i * 3) % (max(1, n // 2))
        l1.append(str(val))

    # Core logic from original code
    l2 = []
    for i in l1:
        l2.append(int(i))
    l1 = set(l2)
    l1 = list(l1)
    for i in range(0, len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] > l1[j]:
                temp = l1[j]
                l1[j] = l1[i]
                l1[i] = temp
    if len(l1) > 1:
        # print(l1[1])
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)