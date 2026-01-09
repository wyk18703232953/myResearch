def main(n):
    # Generate deterministic input list l of length n
    # Example pattern: repeating sequence of 0,1,2,...
    l = [i % 3 for i in range(n)]

    i = 0
    ans = 0
    while i < len(l) - 1:
        if l[i] == l[i + 1]:
            i = i + 1
            continue

        j = i + 1
        ind = -1
        while j < len(l):
            if l[j] == l[i]:
                ind = j
                break
            j = j + 1

        while ind > i + 1:
            l[ind], l[ind - 1] = l[ind - 1], l[ind]
            ans += 1
            ind -= 1

        i += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)