def main(n):
    from itertools import permutations as p

    def generate_bits(total_bits):
        # Deterministic bit sequence of length total_bits
        # Pattern: (i * 2 + 1) % 2
        for i in range(total_bits):
            yield (i * 2 + 1) % 2

    def f(n, t):
        a = 0
        f_bit = 1
        total_bits = n * (2 * n)
        gen = generate_bits(total_bits)
        for _ in range(n):
            for _ in range(2 * n):
                x = next(gen)
                if x != f_bit:
                    a += 1
                f_bit = 1 - f_bit
        if t < 3:
            # consume an extra block of n bits deterministically
            extra_bits = n
            gen = generate_bits(extra_bits)
            for _ in range(extra_bits):
                _ = next(gen)
        return a

    m = []
    b = [-1, -1, 1, 1]
    for i in range(4):
        m.append(f(n, i))
    result = 2 * n ** 2 + min(
        sum(x * y for x, y in zip(q, m)) for q in set(p(b))
    )
    print(result)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)