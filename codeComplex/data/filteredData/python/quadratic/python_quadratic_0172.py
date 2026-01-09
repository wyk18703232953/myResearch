def main(n):
    # Deterministically generate n and k, and xs based on n
    # Interpret n as the length of xs
    if n <= 0:
        return

    # Choose k deterministically as a function of n (at least 1)
    k = max(1, n // 3)

    # Generate xs deterministically:
    # Use a mix of small and larger values to exercise branches
    # Values range roughly within [0, 3n]
    xs = [((i * 7) % (3 * n + 1)) for i in range(n)]

    mapka = {}
    lengths = {}

    result = []

    for x in xs:
        if x in mapka:
            result.append(mapka[x])

        else:
            left = max(0, x - k + 1)
            range_potential = x - left
            for i in range(range_potential, -1, -1):
                potential_left = x - i
                if potential_left not in mapka:
                    result.append(potential_left)
                    for y in range(potential_left, x + 1):
                        mapka[y] = potential_left
                    lengths[potential_left] = x - potential_left + 1
                    break

                else:
                    base = mapka[potential_left]
                    if lengths[base] + (x - potential_left) <= k:
                        result.append(base)
                        for y in range(base + lengths[base], x + 1):
                            mapka[y] = base
                            lengths[base] += 1
                        break

    # Final output to keep behavior similar to original program
    # print(' '.join(map(str, result)))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)