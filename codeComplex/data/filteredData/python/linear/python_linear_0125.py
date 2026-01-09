def if_Spruce(n, l, m):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if m[i] == 0:
            d[l[i]] += 1
    for i in range(1, n + 1):
        if m[i] > 0 and d[i] < 3:
            return "No"
    return "Yes"


def main(n):
    if n < 2:
        # print("Yes")
        pass
        return
    l = [0, 0]
    m = [0] * (n + 1)
    for i in range(2, n + 1):
        parent = (i - 2) // 3 + 1
        l.append(parent)
        m[parent] += 1
    # print(if_Spruce(n, l, m))
    pass
if __name__ == "__main__":
    main(10)