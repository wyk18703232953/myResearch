def main(n):
    # Interpret n as both n (size) and m (number of elements), matching original input structure
    m = n
    square = [0] * n
    # Deterministically generate list l of length m with values in [1, n]
    # Use a simple cyclic pattern: 1,2,...,n,1,2,... based on index
    l = [(i % n) + 1 for i in range(m)]
    for x in l:
        square[x - 1] += 1
    # print(min(square))
    pass
if __name__ == "__main__":
    main(10)