def main(n):
    from math import ceil
    k = n + 1 if n > 0 else 1
    result = ceil((n * 2) / k) + ceil((n * 5) / k) + ceil((n * 8) / k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)