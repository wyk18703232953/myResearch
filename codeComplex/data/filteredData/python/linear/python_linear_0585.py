def main(n):
    C = 10**9 + 7

    # Map n to original parameters:
    # - string/list length = n
    # - number of queries q = n
    length = n
    q = n

    # Deterministically generate the binary list 'lst' of length n
    # Example pattern: lst[i] = i % 2
    lst = [i % 2 for i in range(length)]

    # Build prefix counts new_lst as in the original code
    new_lst = [(0, 0)]
    for v in lst:
        if v == 0:
            new_lst.append((new_lst[-1][0] + 1, new_lst[-1][1]))

        else:
            new_lst.append((new_lst[-1][0], new_lst[-1][1] + 1))

    # Precompute powers of 2 modulo C
    ls = [1]
    for _ in range(length):
        ls.append(ls[-1] * 2 % C)

    # Deterministically generate q queries (l, r) with 1 <= l <= r <= n
    # Example: sliding windows of varying sizes
    queries = []
    for i in range(q):
        l = (i % length) + 1
        r = length
        if l > r:
            l, r = r, l
        queries.append((l, r))

    # Process all queries
    result = 0
    for l, r in queries:
        zeros = new_lst[r][0] - new_lst[l - 1][0]
        ones = new_lst[r][1] - new_lst[l - 1][1]
        s = zeros + ones
        result = (result + (ls[s] - ls[zeros])) % C

    # To avoid huge output for large n, only print a single aggregate result
    # print(result)
    pass
if __name__ == "__main__":
    main(10)