def main(n):
    k = n * (n - 1) // 4
    upper_bound = n + 1
    lower_bound = -1
    while upper_bound > lower_bound + 1:
        m = (upper_bound + lower_bound) // 2
        if (n - m) * (n - m + 1) // 2 - m > k:
            lower_bound = m

        else:
            upper_bound = m
    # print(upper_bound)
    pass
if __name__ == "__main__":
    main(10)