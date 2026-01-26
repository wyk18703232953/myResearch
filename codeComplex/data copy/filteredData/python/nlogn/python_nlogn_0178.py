def main(n):
    # Generate deterministic test data of size n
    # Each segment: (x, w)
    # Let x = i, w = (i % 5) + 1 to ensure some overlap/variation
    segments = []
    for i in range(n):
        x = i
        w = (i % 5) + 1
        segments.append((x + w, x - w))  # (end, start)

    if not segments:
        # print(0)
        pass
        return

    segments.sort()

    ans = 0
    t = segments[0][1]
    for end, start in segments:
        if t <= start:
            ans += 1
            t = end

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)