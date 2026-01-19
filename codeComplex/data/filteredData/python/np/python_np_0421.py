def check(mid, n, m, arr):
    masks = {}
    for index in range(n):
        array = arr[index]
        x = 0
        for i in range(m):
            if array[i] >= mid:
                x ^= (1 << i)
        masks[x] = index + 1
    ans = False
    a, b = 1, 1
    full_mask = (1 << m) - 1
    if full_mask in masks:
        return True, (masks[full_mask], masks[full_mask])
    for i in masks.keys():
        for j in masks.keys():
            orAns = i | j
            if orAns == full_mask:
                if i == full_mask and i in masks:
                    a = masks[i]
                    ans = True
                    break
                elif j == full_mask and j in masks:
                    b = masks[j]
                    ans = True
                    break
                elif i in masks and j in masks:
                    ans = True
                    a, b = masks[i], masks[j]
                    break
        if ans:
            break
    return ans, (a, b)

def solve(n, m, arr):
    mini = 0
    maxi = int(1e9) + 5
    i, j = 1, 1
    while mini <= maxi:
        mid = (mini + maxi) // 2
        ans, res = check(mid, n, m, arr)
        if ans:
            i, j = res
            mini = mid + 1
        else:
            maxi = mid - 1
    print(i, j)

def generate_data(n):
    # Map n to matrix dimensions and values deterministically.
    # For scalability, let m grow slowly with n.
    # Ensure m >= 1.
    m = max(1, min(20, n // 2 if n >= 2 else 1))
    arr = []
    base = 10 ** 5
    for i in range(n):
        row = []
        for j in range(m):
            # Fully deterministic arithmetic construction
            val = (i + 1) * (j + 2) + (i // 2) + (j * j) + base
            row.append(val)
        arr.append(row)
    return n, m, arr

def main(n):
    n_gen, m, arr = generate_data(n)
    solve(n_gen, m, arr)

if __name__ == "__main__":
    # Example deterministic call; change n as needed for experiments
    main(10)