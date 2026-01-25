def main(n):
    # Interpret n as the size of the list a
    if n < 0:
        n = 0

    # Deterministic generation of a based on n
    # Example pattern: a[i] = (i // 2)
    a = [i // 2 for i in range(n)]

    pro = n * (n - 1) // 2
    dic = {}
    for item in a:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    counter = 0
    for item in dic:
        if 0 in dic and dic[0] >= 2:
            print('cslnb')
            break
        if dic[item] > 2:
            print('cslnb')
            break
        elif dic[item] == 2:
            if counter == 1 or item - 1 in dic:
                print('cslnb')
                break
            else:
                counter = 1
    else:
        if (sum(a) - pro) % 2 == 1:
            print('sjfnb')
        else:
            print('cslnb')


if __name__ == "__main__":
    # Example deterministic call
    main(10)