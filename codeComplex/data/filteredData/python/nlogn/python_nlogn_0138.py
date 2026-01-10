def main(n):
    # Interpret n as the number of extension cords
    n_extnson = n

    # Deterministically construct number of devices and sockets
    # Ensure at least 1 socket and at least 1 device
    n_sokts = max(1, n // 3)
    n_dvics = max(1, n_sokts + n)  # ensure needing extensions

    # Deterministically construct extensions list of length n_extnson
    # Each extension size is at least 2 (so it's meaningful)
    extensions = [(i % 5) + 2 for i in range(n_extnson)]

    extensions.sort(reverse=True)
    devices_left = n_dvics - n_sokts
    extnson_used = 0
    i = 0
    while devices_left > 0 and n_extnson > 0 and i < len(extensions):
        devices_left += 1
        extnson_siez = extensions[i]
        devices_left -= extnson_siez
        extnson_used += 1
        n_extnson -= 1
        i += 1

    if devices_left > 0:
        print(-1)
    else:
        print(extnson_used)


if __name__ == "__main__":
    main(10)