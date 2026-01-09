def get_array(x, initial=None):
    import copy
    dimension = len(x)
    if dimension == 1:
        return [copy.deepcopy(initial) for _ in range(x[0])]

    else:
        return [get_array(x[1:], initial) for _ in range(x[0])]


def solve_with_generated_data(n):
    # Generate deterministic input:
    # Original input structure:
    #   n
    #   f[0] f[1] ... f[n-1]
    #
    # f[i] is a parent index in [1, n] or 0 (for -1 after shift), we construct a simple pattern.
    # Here we construct:
    #   For i from 0 to n-1:
    #       if i == 0: f[0] = 0  (becomes -1 after shift, root)
    #       else:      f[i] = ((i - 1) % n) + 1
    # This makes a deterministic structure and keeps indices in valid range.
    generated_n = n
    if generated_n <= 0:
        # print("")
        pass
        return
    f = []
    for i in range(generated_n):
        if i == 0:
            f.append(0)

        else:
            f.append(((i - 1) % generated_n) + 1)

    # Core algorithm from original solve()
    new_f = [0] + f
    for i in range(0, generated_n):
        new_f[i] -= 1
    f = new_f

    chs = get_array([generated_n], [])
    for i, p in enumerate(f):
        if p >= 0:
            chs[p].append(i)

    q = [x for x in range(0, generated_n) if not chs[x]]
    vis = [0] * generated_n
    count = [0] * generated_n
    while q:
        x = q.pop(0)
        if not chs[x]:
            count[x] = 1
        if f[x] >= 0:
            vis[f[x]] += 1
            if vis[f[x]] == len(chs[f[x]]):
                q.append(f[x])
            count[f[x]] += count[x]

    count = sorted(count)
    # print(' '.join([str(x) for x in count]))
    pass


def main(n):
    solve_with_generated_data(n)


if __name__ == "__main__":
    main(10)