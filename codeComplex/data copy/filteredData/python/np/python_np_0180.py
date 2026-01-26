from itertools import combinations

def main(n):
    # Interpret n as the number of elements in array a
    if n < 2:
        print(0)
        return

    # Deterministic construction of parameters
    # l, r, x are fixed so that the algorithm has work to do but is deterministic
    l = n
    r = 3 * n
    x = 2

    # Deterministic construction of array a with size n
    a = [i % 10 + (i // 3) for i in range(1, n + 1)]

    # Core algorithm logic preserved from original code
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )
    print(ans)

if __name__ == "__main__":
    main(10)