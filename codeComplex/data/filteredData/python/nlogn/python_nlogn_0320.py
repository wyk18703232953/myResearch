def main(n):
    # Deterministic generation of input structure:
    # Interpret original input as a permutation mapping 1..n, with 1-based indexing and a dummy 0 at front.
    # We'll build a "permutation" a of size n where a[i] is ((i * 2) % n) + 1, ensuring it's within 1..n.
    # To avoid self-loops that could cause infinite cycles in the original logic, adjust when a[i] == i.
    a = [0]
    for i in range(1, n + 1):
        val = (i * 2) % n + 1
        if val == i:
            val = (val % n) + 1
        a.append(val)

    ans = 0
    for i in range(1, len(a)):
        if a[i] == -1:
            continue
        j = i
        while a[j] != -1:
            prev = j
            j = a[j]
            a[prev] = -1
        ans += 1

    if ans % 2 == 0:
        # print("Petr")
        pass

    else:
        # print("Um_nik")
        pass
if __name__ == "__main__":
    main(10)