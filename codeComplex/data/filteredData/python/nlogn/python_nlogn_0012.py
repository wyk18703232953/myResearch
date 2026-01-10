def main(n):
    # n controls the number of existing buildings (exist_num)
    exist_num = n
    # deterministically define new_width based on n
    new_width = n // 2 + 1

    buildings = []
    # deterministically generate (center, width) pairs
    # centers increase with i, widths vary deterministically with i
    for i in range(exist_num):
        center = 3 * i + 1
        width = (i % 5) + 1
        buildings.append((center - width / 2, center + width / 2))

    buildings.sort()
    possible_loc = 2
    for left, right in zip(buildings, buildings[1:]):
        gap = right[0] - left[1]
        if gap == new_width:
            possible_loc += 1
        elif gap > new_width:
            possible_loc += 2

    print(possible_loc)


if __name__ == "__main__":
    main(10)