def main(n):
    # n is the input size; original code reads 2*n numbers
    # Here we deterministically generate an array of length 2*n
    # Pattern: first n numbers appear twice in order -> guarantees pairs
    ar = [i for i in range(n)] * 2  # length = 2*n
    ans = 0
    for i in range(2 * n):
        for j in range(i + 1, 2 * n):
            if ar[i] == ar[j]:
                while j != i + 1:
                    ar[j], ar[j - 1] = ar[j - 1], ar[j]
                    j -= 1
                    ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)