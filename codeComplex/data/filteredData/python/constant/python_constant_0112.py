def main(n):
    # In this refactored version, n itself is treated as the input value
    if n > 0:
        result = n

    else:
        n_abs = -n
        x = n_abs % 10
        y = (n_abs // 10) % 10
        if x > y:
            result = -(n_abs // 10)

        else:
            result = -((n_abs // 100) * 10 + x)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust the value to change input scale
    main(-123)