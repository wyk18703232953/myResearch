def main(n):
    # Interpret n as the length of arr and t, and also set m deterministically.
    # Ensure n >= 2 for meaningful behavior
    if n < 2:
        n = 2

    # Define m deterministically as the number of taxis (positions with t[i] == 1])
    # For simplicity, let m be n//3 + 1, but at least 1
    m = max(1, n // 3 + 1)

    # Generate arr as a strictly increasing sequence of integers
    # arr[i] = i + 1
    arr = [i + 1 for i in range(n)]

    # Generate t: first m positions in arr will be taxis (t[i] = 1), rest 0.
    # To spread taxis somewhat uniformly, place them at indices floor(k * n / (m+1))
    t = [0] * n
    for k in range(1, m + 1):
        idx = (k * n) // (m + 1)
        if idx >= n:
            idx = n - 1
        t[idx] = 1

    taxi = []
    for i in range(len(arr)):
        if t[i] == 1:
            taxi.append(arr[i])

    # If all t are 0 (no taxis), handle separately: print zeros
    if len(taxi) == 0:
        taxi3 = [0] * m
        # print(" ".join(map(str, taxi3)))
        pass
        return

    taxi2 = []
    kek = 1
    for i in range(len(taxi) - 1):
        taxi2.append([kek, taxi[i] + (taxi[i + 1] - taxi[i]) // 2])
        kek = taxi[i] + (taxi[i + 1] - taxi[i]) // 2 + 1
    taxi2.append([kek, arr[-1]])

    taxi3 = [0] * m
    j = 0
    for i in range(len(arr)):
        if j + 1 < len(taxi2) and arr[i] > taxi2[j][1]:
            j += 1
        if t[i] != 1:
            taxi3[j] += 1

    # print(" ".join(map(str, taxi3)))
    pass
if __name__ == "__main__":
    main(10)