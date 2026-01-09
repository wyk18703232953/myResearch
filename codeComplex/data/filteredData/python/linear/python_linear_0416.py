def main(n):
    # n controls the length of the string l
    # We fix k deterministically as roughly n//3 (at least 1)
    k = max(1, n // 3)

    # Deterministically generate a lowercase string of length n
    # Pattern: cyclic letters 'a'..'z'
    l = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    # Core logic from original program
    l = sorted(l)
    ans = l[0]
    total = ord(l[0])
    index = 0
    for j in range(1, n):
        if len(ans) < k:
            if ord(l[j]) - ord(l[index]) > 1:
                ans = ans + l[j]
                total = total + ord(l[j])
                index = j

        else:
            break
    if len(ans) == k:
        total = total - 96 * k
        # print(total)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(1000)