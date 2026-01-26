def main(n):
    def rd_gen(t_index):
        # Deterministic generator based on n and t_index
        for i in range(n):
            yield (i + t_index) % 2

    def f(n, t):
        it = rd_gen(t)
        a = sum(((i + j) & 1) == x for i in range(n) for j, x in enumerate(it))
        if t < 3:
            # consume one more sequence deterministically
            for _ in rd_gen(t + 1000):
                pass
        return a

    m = sorted([f(n, i) for i in range(4)])
    return 2 * n * n + m[0] + m[1] - m[2] - m[3]


if __name__ == "__main__":
    # print(main(5))
    pass