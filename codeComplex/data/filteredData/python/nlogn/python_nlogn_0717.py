def shuntsu(li):
    li.sort()
    return (
        li[0][1] == li[1][1]
        and li[1][1] == li[2][1]
        and int(li[1][0]) == int(li[0][0]) + 1
        and int(li[2][0]) == int(li[1][0]) + 1
    )


def core_logic(l):
    if l[0] == l[1] and l[1] == l[2]:
        return 0
    if shuntsu(l[:]):
        return 0
    for k in l:
        if len([x for x in l if x == k]) > 1:
            return 1
        if len([x for x in l if x[1] == k[1] and int(x[0]) == int(k[0]) + 1]) != 0:
            return 1
        if len([x for x in l if x[1] == k[1] and int(x[0]) == int(k[0]) + 2]) != 0:
            return 1
    return 2


def generate_input(n):
    # Deterministically generate a list of 3 tile strings like "1m", "2p", etc.
    # Use n to vary the numbers and suits in a predictable way.
    suits = ['m', 'p', 's']  # three suits
    # Ensure values between 1 and 9
    a = (n % 9) + 1
    b = ((2 * n) % 9) + 1
    c = ((3 * n) % 9) + 1
    sa = suits[n % 3]
    sb = suits[(n // 3) % 3]
    sc = suits[(n // 9) % 3]
    l = [str(a) + sa, str(b) + sb, str(c) + sc]
    return l


def main(n):
    l = generate_input(n)
    result = core_logic(l)
    print(result)


if __name__ == "__main__":
    main(10)