def main(n):
    # Generate deterministic input: n and arr of length n
    # Example: arr[i] = (i * 3 + 5) % (2 * n + 1) + 1 to avoid zeros
    arr = [((i * 3 + 5) % (2 * n + 1)) + 1 for i in range(n)]

    arr.sort(reverse=True)

    d = {}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]].append(i)
        else:
            d[arr[i]] = [i]

    cnt = 0
    vis = [-1] * n
    for i in range(n):
        s = bin(arr[i])
        s = s[2:]
        s = s[::-1]
        l = len(s)
        x = 0
        for j in range(l):
            if s[j] == "0":
                x = x + (2 ** j)
        x = x + 1

        if x in d:
            if x == arr[i] and len(d[x]) == 1:
                if vis[i] == -1:
                    cnt = cnt + 1
            else:
                if vis[d[x][0]] == -1:
                    for j in d[x]:
                        vis[j] = 1
        else:
            if vis[i] == -1:
                cnt = cnt + 1
        vis[i] = 1

    print(cnt)


if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)