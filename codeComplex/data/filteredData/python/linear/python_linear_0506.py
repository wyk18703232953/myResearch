def wins(mem, l, pos):
    if mem[pos] != 0:
        return mem[pos] == 1

    val = l[pos]

    lo = pos - val
    while lo >= 0:
        if l[lo] > val and not wins(mem, l, lo):
            mem[pos] = 1
            return True
        lo -= val

    hi = pos + val
    while hi < len(l):
        if l[hi] > val and not wins(mem, l, hi):
            mem[pos] = 1
            return True
        hi += val

    mem[pos] = 2
    return False


def generate_input(n):
    # Deterministic construction: l[i] = (i % 5) + 1, length = n
    l = [((i % 5) + 1) for i in range(n)]
    return l


def main(n):
    l = generate_input(n)
    mem = [0 for _ in range(n)]
    ans = ""
    for i in range(n):
        ans += "A" if wins(mem, l, i) else "B"
    print(ans)


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)