def main(n):
    # n controls the length of the aliens string and seat_rows
    # Generate deterministic seat_rows and aliens based on n
    seat_rows = [(i * 3 + 1) % (n + 5) for i in range(n)]
    aliens = ''.join('0' if i % 2 == 0 else '1' for i in range(n))

    eldian = "0"
    marleyan = "1"

    empty = sorted(enumerate(seat_rows), key=lambda x: x[1], reverse=True)
    non_empty = []

    result = []
    for alien in aliens:
        if alien == eldian:
            row = empty.pop()
            non_empty.append(row)
        else:
            if non_empty:
                row = non_empty.pop()
            else:
                # If no non_empty is available, fall back to empty to keep it total
                if empty:
                    row = empty.pop()
                    non_empty.append(row)
                else:
                    # Degenerate case, no rows; use a dummy
                    row = (0, 0)
        result.append(row[0] + 1)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main(10)