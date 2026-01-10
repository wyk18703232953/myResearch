def main(n):
    # Deterministically generate t based on n
    # For example, let t be a small fixed value related to n
    t = (n % 5) + 1  # t in [1,5]

    # Generate n intervals with deterministic centers and lengths
    # Centers increase linearly, lengths vary deterministically
    cont = []
    for i in range(n):
        hCenter = float(i * 3)  # centers at 0,3,6,9,...
        hLen = float((i % 4) + 1)  # lengths cycle through 1,2,3,4
        cont.append([hCenter - hLen / 2.0, hCenter + hLen / 2.0])

    ans = 2
    cont.sort(key=lambda item: item[0])

    for i in range(n - 1):
        gap = cont[i + 1][0] - cont[i][1]
        if gap > t:
            ans += 2
        elif gap == t:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main(10)