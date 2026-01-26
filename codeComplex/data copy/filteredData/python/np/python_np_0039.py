from math import factorial

def main(n):
    # Deterministically generate drazil and dreamoon based on n.
    # Map n to string length.
    length = max(1, n)

    # drazil: first half '+', second half '-'
    half = length // 2
    drazil = ''.join('+' if i < half else '-' for i in range(length))

    # dreamoon: cycle through '+', '-', '?'
    pattern = ['+', '-', '?']
    dreamoon = ''.join(pattern[i % 3] for i in range(length))

    net_drazil = 0
    net_dreamoon = 0
    uncretain_count = 0

    for ch in drazil:
        if ch == '-':
            net_drazil -= 1
        else:
            net_drazil += 1

    for ch in dreamoon:
        if ch == '-':
            net_dreamoon -= 1
        elif ch == '+':
            net_dreamoon += 1
        else:
            uncretain_count += 1

    diff = net_drazil - net_dreamoon
    x = (uncretain_count + diff) // 2
    y = (uncretain_count - diff) // 2

    if abs(x) + abs(y) != uncretain_count or x < 0 or x > uncretain_count:
        print(0.0)
    else:
        out = factorial(uncretain_count) // (factorial(x) * factorial(uncretain_count - x))
        print(out / (2 ** uncretain_count))


if __name__ == "__main__":
    main(10)