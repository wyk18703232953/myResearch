from collections import deque

def generate_input(n):
    # Ensure n is at least 1
    n = max(1, int(n))
    # Generate a deterministic array a of length n with values in [1, n]
    # Example pattern: a[i] = (i % n) + 1
    a = [(i % n) + 1 for i in range(n)]
    return n, a

def main(n):
    n, a = generate_input(n)

    # Core logic from original program, adapted to generated input
    bs = set()
    moves = {}
    for i in range(n):
        moves[a[i]] = [a[j] for j in range(i % a[i], n, a[i]) if a[j] > a[i]]
    winners = {}
    for i in range(n, 0, -1):
        winner = 'A' if any(winners[j] == 'B' for j in moves[i]) else 'B'
        if winner == 'B':
            bs.add(i)
        winners[i] = winner
    print(''.join(winners[ai] for ai in a))


if __name__ == "__main__":
    main(10)