def main(n):
    # Deterministically generate input:
    # Original structure:
    #   n : integer
    #   a : list of n integers
    # Here we let a be a list of length n with a simple pattern.
    # To allow some duplicates and 0s while scaling with n, use modulo.
    a = [i % (n // 2 + 1) if n > 1 else 0 for i in range(n)]

    total = sum(a)
    final = n * (n - 1) // 2
    repeated = []
    count = {}

    for i in a:
        try:
            count[i] += 1
            repeated.append(i)
        except KeyError:
            count[i] = 1

    moves = total - final

    if len(repeated) > 1:
        # print('cslnb')
        pass
    elif 0 in repeated:
        # print('cslnb')
        pass
    elif len(repeated) == 1 and repeated[0] - 1 in a:
        # print('cslnb')
        pass

    else:
        if moves % 2 == 0 or moves <= 0:
            # print('cslnb')
            pass

        else:
            # print('sjfnb')
            pass
if __name__ == "__main__":
    main(10)