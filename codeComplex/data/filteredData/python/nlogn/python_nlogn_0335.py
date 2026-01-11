def main(n):
    # Generate deterministic test data based on n
    # Create n strings where each is a prefix of the next, to trigger "YES" behavior
    li = []
    for i in range(1, n + 1):
        # Construct a string pattern: 'a', 'aa', 'aaa', ...
        s = "a" * i
        li.append(s)

    lst2 = sorted(li, key=len)
    c = 1
    for i in range(len(lst2) - 1):
        if lst2[i] not in lst2[i + 1]:
            c = 0
    if c == 1:
        # print("YES")
        pass
        for j in lst2:
            # print(j)
            pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(5)