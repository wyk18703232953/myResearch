def main(n):
    # Interpret n as both the length of the list and m (number of selected elements)
    # Generate a deterministic list lst of length n
    # Example: lst[i] = (i * 3 + 1) % (n + 7) + 1 to avoid too many duplicates and keep positive
    lst = [((i * 3 + 1) % (n + 7)) + 1 for i in range(n)]
    m = n

    arr = lst.copy()
    arr.sort(reverse=True)
    vis = [0] * n
    summ = 0
    upper = m if m <= n else n
    for i in range(upper):
        temp = arr[i]
        summ += temp
        for j in range(n):
            if vis[j] == 0 and lst[j] == temp:
                vis[j] = 1
                break

    print(summ)
    cnt = 0
    ans = []
    for i in range(n):
        if vis[i] == 1:
            ans.append(cnt + 1)
            cnt = 0
        else:
            cnt += 1
    if ans:
        ans[-1] += cnt
    print(*ans)


if __name__ == "__main__":
    main(10)