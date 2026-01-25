def solve(num_pixels, max_group_size, pixels):
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

    print(*(groups[pixel] for pixel in pixels))


def main(n):
    if n <= 0:
        return

    # Map n to input scale:
    # - number of pixels = n
    # - max_group_size is a deterministic function of n, bounded [1, 256]
    num_pixels = n
    max_group_size = (n % 256) + 1

    # Generate a deterministic list of pixels in [0, 255]
    # Pattern: pixels[i] = (i * 37 + 13) % 256
    pixels = [(i * 37 + 13) % 256 for i in range(num_pixels)]

    solve(num_pixels, max_group_size, pixels)


if __name__ == "__main__":
    main(10)