def main(n):
    # Interpret n as the number of segments
    # Deterministically generate n segments (l, r)
    # Example pattern:
    # segment i: [i, i + (i % 5) + 1]
    segments = []
    for i in range(n):
        l = i
        r = i + (i % 5) + 1
        segments.append((l, r, i + 1))

    # Sort segments by (l, r, idx) as in original code
    segments = sorted((s[0], s[1], s[2]) for s in segments)

    prev = (-1, -1, -1)
    for segment in segments:
        assert prev[0] <= segment[0]
        if prev[0] == segment[0]:
            assert prev[1] <= segment[1]
            # print(prev[2], segment[2])
            pass
            break
        elif prev[1] >= segment[1]:
            # print(segment[2], prev[2])
            pass
            break
        prev = segment

    else:
        # print(-1, -1)
        pass
if __name__ == "__main__":
    main(10)