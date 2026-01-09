def main(n):
    # Scale definition:
    # num_pixels = n
    # max_group_size cycles deterministically between 1 and 10
    num_pixels = n
    if num_pixels <= 0:
        return
    max_group_size = (n % 10) + 1

    # Deterministic pixel generation in range [0, 255]
    pixels = [(i * 37 + 13) % 256 for i in range(num_pixels)]
    groups = [None for _ in range(256)]

    for pixel in pixels:
        if groups[pixel] is None:
            smallest_of_group = pixel
            while (
                smallest_of_group >= 0
                and smallest_of_group > pixel - max_group_size
                and groups[smallest_of_group] is None
            ):
                smallest_of_group -= 1

            if (
                smallest_of_group >= 0
                and groups[smallest_of_group] is not None
                and pixel - groups[smallest_of_group] + 1 <= max_group_size
            ):
                group_color = groups[smallest_of_group]

            else:
                group_color = smallest_of_group + 1

            smallest_of_group += 1
            for color in range(smallest_of_group, pixel + 1):
                groups[color] = group_color

    output = [groups[pixel] for pixel in pixels]
    # print(*output)
    pass
if __name__ == "__main__":
    main(1000)