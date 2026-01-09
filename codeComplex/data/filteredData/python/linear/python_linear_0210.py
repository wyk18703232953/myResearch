def main(n):
    from collections import defaultdict

    # Deterministic parameter generation
    # Original input: n, a1, b
    # Let a1 and b be simple functions of n
    a1 = n % 10 + 1
    b_param = n % 7 + 1

    # Generate n triplets (a, b_val, c) deterministically
    # Original code only uses b and c from these triplets
    d = defaultdict(int)
    for i in range(n):
        a = i  # unused in logic, but kept structurally
        b_val = (i % (n // 2 + 1)) + 1
        c_val = (i * a1 + b_val * b_param) // 2
        d[(b_val, c_val)] += 1

    e = defaultdict(list)
    e1 = defaultdict(int)
    ans = 0

    # Same aggregation logic as original
    for key in d:
        b_val, c_val = key
        idx = c_val - a1 * b_val
        e[idx].append(d[key])
        e1[idx] += d[key]

    for idx in e:
        total = e1[idx]
        for count in e[idx]:
            ans += count * (total - count)

    # Return result so caller can use it in experiments
    return ans


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    result = main(1000)
    # print(result)
    pass