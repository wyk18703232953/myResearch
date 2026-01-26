def main(n):
    # Generate deterministic test data for given n
    # Here: piles is a list of length n with increasing integers, then reversed to introduce some variability
    # Example generation: [i // 2 for i in range(n)] ensures duplicates and sorted-like behavior
    piles = [i // 2 for i in range(n)]
    # The original code sorts piles at the beginning, so order before this point doesn't matter
    piles.sort()

    num = piles[0] if n > 0 else 0
    count = 1
    two = 0
    two_num = 0

    for i in range(1, n):
        if piles[i] == num:
            count += 1

        else:
            if count > 2:
                # print('cslnb')
                pass
                return
            elif count == 2:
                two_num = num
                two += 1
            num = piles[i]
            count = 1

    if n > 0:
        if count == 2:
            two_num = num
            two += 1
        if count > 2:
            # print('cslnb')
            pass
            return
    if two > 1:
        # print('cslnb')
        pass
        return

    if two == 1:
        if (two_num - 1) in piles:
            # print('cslnb')
            pass
            return

    if n >= 2:
        if piles[0] == piles[1] and piles[0] == 0:
            # print('cslnb')
            pass
            return

    moves = 0
    curr = 0
    for i in range(n):
        if piles[i] >= curr:
            moves += piles[i] - curr
            piles[i] = curr
            curr += 1

    for x in piles:
        if x > 0:
            moves += 1
            break

    if n == 1:
        moves += 1

    if moves % 2 != 0:
        # print('cslnb')
        pass

    else:
        # print('sjfnb')
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(10)