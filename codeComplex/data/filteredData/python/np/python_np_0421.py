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
    if (1 << m) - 1 in masks:
        return True, (masks[(1 << m) - 1], masks[(1 << m) - 1])
    for i in masks.keys():
        for j in masks.keys():
            orAns = i | j
            if orAns == ((1 << m) - 1):
                if i == (1 << m) - 1 and (i in masks):
                    a = masks[i]
                    ans = True
                    break
                elif j == (1 << m) - 1 and (j in masks):
                    b = masks[j]
                    ans = True
                    break
                elif (i in masks) and (j in masks):
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
    # Map n to a square matrix n x n
    m = n
    arr = [[(i + 1) * (j + 1) for j in range(m)] for i in range(n)]
    return n, m, arr

def main(n):
    n_gen, m_gen, arr = generate_data(n)
    solve(n_gen, m_gen, arr)

if __name__ == "__main__":
    main(5)