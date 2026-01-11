def main(n):
    # Deterministically generate n segments (l, r, index)
    # Example pattern: segments with increasing starts and varying ends
    segments = []
    for i in range(n):
        # Start point increases with i
        x = i
        # End point is constructed deterministically but may create nesting
        # Using a simple pattern: r = i + (i % 3) + 1
        y = i + (i % 3) + 1
        segments.append((x, y, i + 1))

    segments = sorted(segments, key=lambda x: (x[0], -x[1]))

    for i, seg in enumerate(segments):
        j = i + 1
        if j >= n:
            # print("-1 -1")
            pass
            return

        while segments[j][1] <= seg[1]:
            # print(f"{segments[j][2]} {seg[2]}")
            pass
            return

    # print("-1 -1")
    pass
    return


if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)