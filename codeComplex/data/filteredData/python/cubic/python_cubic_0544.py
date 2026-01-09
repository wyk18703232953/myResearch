def main(n):
    # n controls length of string sa; sb will have the same length
    if n <= 0:
        return

    # Deterministic generation of sa (as a string of digits)
    # Pattern: digits cycling 0-9
    sa_str = ''.join(str(i % 10) for i in range(n))
    sa = sorted(sa_str, reverse=True)
    na = len(sa)

    # Deterministic generation of sb
    # Here we reverse sa_str and then sort ascending to keep same digits
    base_sb = sa_str[::-1]
    sb = ''.join(sorted(base_sb))
    nb = len(sb)

    if nb > na:
        # print(''.join(sa))
        pass
        return

    ans = ''
    while sa:
        for i in range(len(sa)):
            new = ans + sa[i] + ''.join(sorted(sa[:i] + sa[i+1:]))
            if int(new) <= int(sb):
                ans += sa[i]
                sa.pop(i)
                break
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)