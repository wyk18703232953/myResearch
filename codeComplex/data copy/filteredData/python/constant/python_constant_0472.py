def main(n):
    # Interpret n as the maximum coordinate magnitude
    # Generate deterministic positions based on n
    # Queen at the origin for simplicity
    q_x, q_y = 0, 0

    # Knight position
    k_x = n
    k_y = -n

    # Destination position
    dest_x = -n
    dest_y = n

    def sign(x):
        return 1 if x >= 0 else -1

    def which_square(x, y):
        return sign(x - q_x), sign(y - q_y)

    if which_square(k_x, k_y) == which_square(dest_x, dest_y):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)