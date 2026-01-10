def main(n):
    # n controls the scale:
    # N = number of boys, M = number of sweets per boy, len(G) = number of girls
    # We construct them deterministically from n.
    if n < 1:
        n = 1

    N = n
    M = max(1, n // 2)
    K = max(1, n)  # number of girls

    # Deterministic construction of capacities
    # Boys' capacities B: descending pattern with some repetition/variation
    B = [(i * 2 + 3) % (3 * n + 5) + 1 for i in range(N)]
    # Girls' requirements G: another deterministic pattern
    G = [(i * 3 + 1) % (3 * n + 7) + 1 for i in range(K)]

    # Core logic from original program
    B.sort(reverse=True)
    G.sort(reverse=True)

    if B[0] > G[-1]:
        print(-1)
        return

    boy_capacities = [M - 1] * N
    current_capable_boy_index = 0
    result = sum(B) * M

    for g in G:
        yet = True
        while yet:
            if B[current_capable_boy_index] < g and boy_capacities[current_capable_boy_index] > 0:
                result += g - B[current_capable_boy_index]
                boy_capacities[current_capable_boy_index] -= 1
                yet = False
            elif B[current_capable_boy_index] == g:
                result += g - B[current_capable_boy_index]
                yet = False
            else:
                current_capable_boy_index += 1
                if current_capable_boy_index > N - 1:
                    print(-1)
                    return

    print(result)


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)