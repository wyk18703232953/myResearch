def main(n):
    # Interpret n as the length t of the array arr
    t = max(1, n)
    # Deterministically set d based on n
    d = n % 10 + 1
    # Deterministically generate arr of length t
    arr = [i * d for i in range(t)]
    # Core logic from original program
    count = 0
    for i in range(t - 1):
        if arr[i + 1] - arr[i] == 2 * d:
            count += 1
        elif arr[i + 1] - arr[i] > 2 * d:
            count += 2
    # print(count + 2)
    pass
if __name__ == "__main__":
    main(10)