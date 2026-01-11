def main(n):
    # Generate deterministic input array 'a' of length n
    # Example pattern: a[i] = (i * 3) % (n + 5)
    a = [(i * 3) % (n + 5) for i in range(n)]
    b = sorted(a)

    diffs = []
    for i in range(n):
        if a[i] != b[i]:
            diffs.append(i)

    if len(diffs) > 2:
        # print("NO")
        pass
    elif not diffs:
        # print("YES")
        pass

    else:
        i, j = diffs
        if a[i] == b[j] and b[i] == a[j]:
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)