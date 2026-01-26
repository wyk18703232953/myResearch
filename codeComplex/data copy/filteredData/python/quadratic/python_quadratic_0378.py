def main(n):
    # Interpret n as both the number of rows and columns of the grid
    rows = n
    cols = n

    top = [-1, -1]
    bottom = [-1, -1]

    for i in range(rows):
        if i == rows // 2:
            # Create a row with a contiguous block of 'B's in the middle
            s = ''.join('B' if cols // 4 <= j < cols - cols // 4 else 'W' for j in range(cols))

        else:
            s = 'W' * cols

        left = s.find('B')
        if left != -1:
            right = s.rfind('B')
            c = (right - left) // 2 + 1
            # Print 1-based coordinates
            # print(i + c, left + c)
            pass
            break


if __name__ == "__main__":
    main(8)