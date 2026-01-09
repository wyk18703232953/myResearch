def main(n):
    # Deterministic data generation:
    # Interpret n as the length of the list.
    # Construct a list with a simple pattern that may include duplicates.
    # Example: lst[i] = (i // 2) for i in range(n)
    lst = [i // 2 for i in range(n)]

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
        # print('cslnb')
        pass
        return

    if not flag:
        if (sum(lst) - sum1) % 2 == 0:
            # print('cslnb')
            pass

        else:
            # print('sjfnb')
            pass

    else:
        if (lol - 1) in lst or lol == 0:
            # print('cslnb')
            pass

        else:
            if (sum(lst) - sum1) % 2 == 0:
                # print('cslnb')
                pass

            else:
                # print('sjfnb')
                pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)