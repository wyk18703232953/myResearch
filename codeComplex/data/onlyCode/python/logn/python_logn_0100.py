def solve(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    ba = bin(a)[2:]
    bb = bin(b)[2:]
    r = ''
    if len(ba) != len(bb):
        int('1' * len(bb), 2)
    else:
        for ca, cb in zip(ba, bb):
            if ca == cb:
                r += '0'
            else:
                r += '1'
                break
    r += '1' * (len(bb) - len(r))
    return int(r, 2)


# assert solve(32473107276976561, 588384394540535099) == 1152921504606846975
# assert solve(1, 2) == 3
# assert solve(1, 1) == 0
# assert solve(8, 16) == 31
# assert solve(506, 677) == 1023
# assert solve(33, 910) == 1023
a, b = map(int, input().split())
print(solve(a, b))
