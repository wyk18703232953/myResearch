import sys

def main(n):
    # Deterministically construct n, k, xs based on input size n
    if n <= 0:
        return

    # Let k grow slowly with n, but at least 1
    k = max(1, n // 3)

    # xs is a list of length n with repeating pattern in a small range
    # Values stay in a moderate range so the map/dict stays meaningful
    xs = [(i * 7) % (2 * n + 1) for i in range(n)]

    # Original algorithm starts here
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
                    if lengths[mapka[potential_left]] + (x - potential_left) <= k:
                        result.append(mapka[potential_left])
                        for y in range(mapka[potential_left] + lengths[mapka[potential_left]], x + 1):
                            mapka[y] = mapka[potential_left]
                            lengths[mapka[potential_left]] += 1
                        break

    # print(' '.join(map(str, result)))
    pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10000)