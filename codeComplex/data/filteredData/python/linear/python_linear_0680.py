def main(n):
    # Generate deterministic input array b of length n
    if n <= 0:
        return
    b = [i * 2 + 1 for i in range(n)]

    a1 = [0]
    a2 = [b[0]]

    for x in b[1:]:
        new_a = a1[-1]
        if x - new_a > a2[-1]:
            new_a = x - a2[-1]
        new_a2 = x - new_a
        a1.append(new_a)
        a2.append(new_a2)

    # print(*(a1 + a2[::-1]))
    pass
if __name__ == "__main__":
    main(10)