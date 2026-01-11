def main(n):
    lst = [(i * 2 + 1) % (n + 3) + 1 for i in range(n)]
    p = max(lst)
    ind = lst.index(p)
    if p == 1:
        lst[ind] = 2

    else:
        lst[ind] = 1
    lst.sort()
    for j in range(n):
        # print(lst[j], end=" ")
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)