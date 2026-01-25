def main(n):
    # Generate deterministic input based on n
    # Interpret n as the length of the list
    if n <= 0:
        return

    # Deterministic list generation:
    # For time complexity experiments, we can generate a pattern
    # that sometimes contains duplicates to exercise all branches.
    # Example: lst[i] = (i // 2)
    lst = [(i // 2) for i in range(n)]

    st = set()
    flag = False
    count = 0
    lol = None

    for i in lst:
        if i not in st:
            st.add(i)
        else:
            flag = True
            count += 1
            lol = i

    sum1 = n * (n - 1) // 2

    if count > 1:
        print('cslnb')
        return

    if not flag:
        if (sum(lst) - sum1) % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')
    else:
        if (lol - 1) in lst or lol == 0:
            print('cslnb')
        else:
            if (sum(lst) - sum1) % 2 == 0:
                print('cslnb')
            else:
                print('sjfnb')


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    for size in [1, 2, 3, 4, 5, 10]:
        main(size)