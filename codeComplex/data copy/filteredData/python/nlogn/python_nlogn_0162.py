def main(n):
    # Deterministically construct w, h based on n
    # Ensure w, h >= 2 and reasonably proportional to n
    w = max(2, n // 2 + 2)
    h = max(2, n // 2 + 3)

    # Initialize arrays as in original code
    l, r = [-1] * (w + 1), [-1] * (w + 1)
    t, b = [-1] * (h + 1), [-1] * (h + 1)
    l[0], b[0], t[h], r[w] = 0, 0, h, w
    V, H = [0] * n, [0] * n

    # Deterministically generate sequence of cuts:
    # Alternate 'V' and 'H', with indices cycling through valid ranges
    for i in range(n):
        if i % 2 == 0:
            line = 'V'
            if w > 1:
                idx = i % (w - 1) + 1

            else:
                idx = 1
            r[idx] = w
            V[i] = idx

        else:
            line = 'H'
            if h > 1:
                idx = i % (h - 1) + 1

            else:
                idx = 1
            t[idx] = h
            H[i] = idx

    left, max_w = 0, 0
    for i in range(1, w + 1):
        if r[i] != -1:
            l[i] = left
            r[left] = i
            max_w = max(max_w, i - left)
            left = i

    bottom, max_h = 0, 0
    for i in range(1, h + 1):
        if t[i] != -1:
            b[i] = bottom
            t[bottom] = i
            max_h = max(max_h, i - bottom)
            bottom = i

    res = [0] * n
    res[n - 1] = max_h * max_w
    for i in range(n - 1, 0, -1):
        if V[i] != 0:
            max_w = max(max_w, r[V[i]] - l[V[i]])
            r[l[V[i]]] = r[V[i]]
            l[r[V[i]]] = l[V[i]]

        else:
            max_h = max(max_h, t[H[i]] - b[H[i]])
            b[t[H[i]]] = b[H[i]]
            t[b[H[i]]] = t[H[i]]
        res[i - 1] = max_h * max_w

    for i in range(n):
        # print(res[i])
        pass
if __name__ == "__main__":
    main(10)