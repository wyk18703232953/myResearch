def main(n):
    # Interpret n as both the number of bits to print and the number of rows in arr
    m = n
    arr = []
    # Deterministic generation of m rows, each row having 2 integers (similar to original input structure)
    for i in range(m):
        # Example deterministic pattern: [i, i ^ 1]
        arr.append([i, i ^ 1])

    k = 0
    ans = str()
    for i in range(n):
        ans += str(k ^ 1)
        k = k ^ 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)