def main(n):
    # n controls the size of the input:
    # m = n (number of taxis to count)
    # length of arr and t = max(n, 2) to avoid degenerate very small cases
    if n < 1:
        return

    m = n
    length = max(n, 2)

    # Deterministic generation of arr: strictly increasing sequence
    # arr[i] = i + 1
    arr = [i + 1 for i in range(length)]

    # Deterministic generation of t: binary pattern with at least one '1'
    # t[i] = 1 if i % 3 == 0 else 0
    t = [1 if i % 3 == 0 else 0 for i in range(length)]

    # Ensure there is at least one taxi (1 in t)
    if all(x == 0 for x in t):
        t[0] = 1

    taxi = []
    for i in range(len(arr)):
        if t[i] == 1:
            taxi.append(arr[i])

    taxi2 = []
    kek = 1
    for i in range(len(taxi) - 1):
        mid = taxi[i] + (taxi[i + 1] - taxi[i]) // 2
        taxi2.append([kek, mid])
        kek = mid + 1
    taxi2.append([kek, arr[-1]])

    taxi3 = [0] * m
    j = 0
    for i in range(len(arr)):
        if j < len(taxi2) - 1 and arr[i] > taxi2[j][1]:
            j += 1
        if t[i] != 1 and j < m:
            taxi3[j] += 1

    # print(" ".join(map(str, taxi3)))
    pass
if __name__ == "__main__":
    main(10)