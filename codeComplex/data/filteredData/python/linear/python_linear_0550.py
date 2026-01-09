def main(n):
    # Deterministic data generation: array length = n
    # a[i] = i for i in 0..n-1
    a = [i for i in range(n)]

    mx = -1
    ans = -1
    for i in range(n):
        if a[i] > mx + 1:
            ans = i + 1
            break

        else:
            mx = max(mx, a[i])
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)