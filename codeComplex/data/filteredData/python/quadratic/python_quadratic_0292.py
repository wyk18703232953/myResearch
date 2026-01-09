def main(n):
    # Interpret n as the number of pairs; hence total elements = 2 * n
    N = n
    if N <= 0:
        # print(0)
        pass
        return

    # Deterministic construction of "pairs" list of length 2*N
    # Pattern: two occurrences of each value from 1..N, arranged in a fixed non-trivial order
    # Example for N=4: [1,2,3,4,1,2,3,4]
    pairs = [i % N + 1 for i in range(2 * N)]

    visited = [False] * (N + 1)
    minimumSwaps = 0

    for i in range(2 * N):
        if not visited[pairs[i]]:
            visited[pairs[i]] = True
            count = 0
            for j in range(i + 1, 2 * N):
                if not visited[pairs[j]]:
                    count += 1
                elif pairs[i] == pairs[j]:
                    minimumSwaps += count

    # print(minimumSwaps)
    pass
if __name__ == "__main__":
    main(10)