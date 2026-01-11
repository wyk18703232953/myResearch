def main(n):
    # Map n to problem parameters deterministically
    # Choose width and height as simple functions of n
    w = n + 3
    h = 2 * n + 5
    cuts = n

    l, r = [-1] * (w + 1), [-1] * (w + 1)
    t, b = [-1] * (h + 1), [-1] * (h + 1)
    l[0], b[0], t[h], r[w] = 0, 0, h, w
    V, H = [0] * cuts, [0] * cuts

    # Deterministic generation of cut operations
    # Alternate between vertical and horizontal cuts
    # Vertical cuts: positions from 1 to w-1
    # Horizontal cuts: positions from 1 to h-1
    v_pos = 1
    h_pos = 1
    for i in range(cuts):
        if i % 2 == 0:
            if v_pos < w:
                V[i] = v_pos
                v_pos += 1

            else:
                # If vertical positions exhausted, use horizontal
                if h_pos < h:
                    H[i] = h_pos
                    h_pos += 1

        else:
            if h_pos < h:
                H[i] = h_pos
                h_pos += 1

            else:
                # If horizontal positions exhausted, use vertical
                if v_pos < w:
                    V[i] = v_pos
                    v_pos += 1

    # Initialize r and t arrays based on generated cuts
    for i in range(cuts):
        if V[i] != 0:
            idx = V[i]
            r[idx] = w
        if H[i] != 0:
            idx = H[i]
            t[idx] = h

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

    res = [0] * cuts
    if cuts > 0:
        res[cuts - 1] = max_h * max_w
        for i in range(cuts - 1, 0, -1):
            if V[i] != 0:
                max_w = max(max_w, r[V[i]] - l[V[i]])
                r[l[V[i]]] = r[V[i]]
                l[r[V[i]]] = l[V[i]]

            else:
                max_h = max(max_h, t[H[i]] - b[H[i]])
                b[t[H[i]]] = b[H[i]]
                t[b[H[i]]] = t[H[i]]
            res[i - 1] = max_h * max_w

    for i in range(cuts):
        # print(res[i])
        pass
if __name__ == "__main__":
    main(10)