def main(n):
    # n is the number of pairs; original array length is 2*n
    # Deterministic construction of a list of length 2*n
    # Pattern: first n elements are 0..n-1, second n elements are reversed 0..n-1
    a = list(range(n)) + list(reversed(range(n)))
    ans = 0
    for i in range(0, 2 * n, 2):
        if a[i] != a[i + 1]:
            for j in range(i + 1, 2 * n):
                if a[j] == a[i]:
                    for k in range(j, i + 1, -1):
                        a[k], a[k - 1] = a[k - 1], a[k]
                        ans += 1
                    break
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)