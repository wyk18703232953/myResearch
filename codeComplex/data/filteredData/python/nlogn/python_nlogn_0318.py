def main(n):
    # Generate a permutation-like array l of size n with values in [0, n-1]
    # Deterministic construction: a single n-cycle via (i+1)%n
    l = [(i + 1) % n for i in range(n)]

    parity = 0
    explore = set(l)
    while len(explore) > 0:
        x = explore.pop()
        tmp = x
        found = [x]
        while l[tmp] != x:
            tmp = l[tmp]
            found.append(tmp)
        for i in found[1:]:
            explore.remove(i)
        parity ^= (len(found) - 1) % 2

    if parity == n % 2:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    main(10)