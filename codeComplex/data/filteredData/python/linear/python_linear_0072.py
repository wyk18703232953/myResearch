def main(n):
    # Deterministically generate s based on n
    s = n // 2 + 1

    mins = s
    my_dict = {}  # kept to preserve original structure, though unused
    mylist = []

    # n represents the number of (person, floor) pairs
    cnt = n
    while cnt:
        # Deterministic generation of person and floor
        person = cnt
        floor = (cnt * 2) % (n + 1) if n > 0 else 0
        mylist.append(person + floor)
        cnt -= 1

    if mylist:
        val = max(mylist)

    else:
        val = 0

    if val < mins:
        # print(mins)
        pass

    else:
        # print(val)
        pass
if __name__ == "__main__":
    main(10)