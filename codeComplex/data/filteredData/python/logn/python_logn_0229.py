def qtd(u):
    ans = 0
    while u > 0:
        u //= 10
        ans += 1
    return ans

def digitos(u):
    ans = 0
    while u > 0:
        ans += u % 10
        u //= 10
    return ans

def core_logic(n_str, m):
    number = int(n_str)
    ans = 0
    size_n = qtd(m)
    i = m

    while i < m + (size_n * 9) + 1:
        if i > number:  # n cannot be greater than m
            break
        if i - digitos(i) >= m:  # check digits
            ans += 1
        i += 1

    if i > number:
        return ans

    else:
        return number - i + 1 + ans

def main(n):
    # Interpret n as the upper bound "number"
    # Generate m deterministically as n // 2 (but at least 1)
    if n < 1:
        return 0
    number_str = str(n)
    m = max(1, n // 2)
    result = core_logic(number_str, m)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(1000000)