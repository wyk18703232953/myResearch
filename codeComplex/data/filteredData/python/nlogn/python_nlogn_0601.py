def main(n):
    # Interpret n as the number of stacks
    # Generate a deterministic non-decreasing sequence of stack heights
    # Example: heights grow roughly linearly with some variation using integer ops
    if n <= 0:
        print(0)
        return

    # Deterministic data generation
    stacks = [(i * 3 + (i // 2)) % (2 * n + 1) + 1 for i in range(n)]
    stacks.sort()

    m = n  # not used in original logic, but kept for structural consistency

    ans = 0
    cur_stack = 0
    cur_h = 0

    while cur_stack < n:
        ans += 1
        if stacks[cur_stack] >= cur_h + 1:
            cur_h += 1
        cur_stack += 1
    ans += stacks[-1] - cur_h

    print(sum(stacks) - ans)


if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)