def listtostring(string):
    return ''.join(str(ele) for ele in string)

def core_algorithm(a, b):
    n = len(a)
    a.sort()
    for i in range(n):
        for j in range(n):
            t = a.copy()
            t[i], t[j] = t[j], t[i]
            if int(listtostring(t)) >= int(listtostring(a)) and int(listtostring(t)) <= int(listtostring(b)):
                a[i], a[j] = a[j], a[i]
    return listtostring(a)

def main(n):
    if n <= 0:
        return ""

    a = [str((i % 10)) for i in range(1, n + 1)]
    a.sort()
    a_str = ''.join(a)
    a_int = int(a_str)

    # Construct b as a larger number with same length
    # Ensure b >= a by adding 1 to the first digit (within 0-9 range)
    first_digit = int(a[0])
    if first_digit < 9:
        b_first = str(first_digit + 1)

    else:
        b_first = '9'
    b = [b_first] + a[1:]
    b_str = ''.join(b)

    result = core_algorithm(list(a_str), list(b_str))
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)