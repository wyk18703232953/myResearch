def main(n):
    # Deterministically generate input list of size n
    # Example pattern: l1[i] = i + 1
    l1 = [i + 1 for i in range(n)]

    ans = 0
    l1.sort()
    visited = [0] * n
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        ans += 1
        for j in range(i + 1, n):
            if visited[j] == 0 and l1[j] % l1[i] == 0:
                visited[j] = 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)