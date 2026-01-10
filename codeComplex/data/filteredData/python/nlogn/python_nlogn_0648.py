from math import *

def bin_search(arr, n):
    pos = -1
    for i in range(35, -1, -1):
        jump = (1 << i)
        if (pos + jump) >= len(arr):
            continue
        if arr[pos + jump] <= n - 1:
            pos += jump
    return len(arr) - pos - 1

def main(n):
    # n controls the size: number of vertical elements and horizontal segments
    # Original parameters: n_vert, m_hor
    n_vert = max(1, n)
    m_hor = max(1, n)

    vert = []
    for i in range(n_vert):
        # deterministic vertical values, increasing but not strictly necessary
        vert.append(i * 2 + 1)

    hor = []
    for i in range(m_hor):
        # simulate col1, col2, row input structure
        # ensure some have col1 == 1 and some not
        col1 = 1 if i % 2 == 0 else 2
        col2 = i + 1
        row = i // 2
        if col1 != 1:
            continue
        hor.append(col2)

    vert.append(1000000000)
    vert = sorted(vert)
    hor = sorted(hor)

    best = int(1e10)
    for i in range(len(vert)):
        cur_ans = bin_search(hor, vert[i]) + i
        if cur_ans < best:
            best = cur_ans

    print(best)

if __name__ == "__main__":
    main(10)