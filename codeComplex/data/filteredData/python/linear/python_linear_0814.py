def main(n):
    # Generate deterministic test data: array of length n
    # Example: arr[i] = i % (n // 2 + 1) to allow duplicates in a controlled way
    if n <= 0:
        return
    arr = [i % (n // 2 + 1) for i in range(n)]

    solved = False
    s = sum(arr)
    if s == 0:
        # print("cslnb")
        pass
        solved = True

    if not solved:
        n_num = {}

        for item in arr:
            if item in n_num:
                n_num[item] += 1

            else:
                n_num[item] = 1

        if 0 in n_num and n_num[0] >= 2:
            # print('cslnb')
            pass
            solved = True

        if not solved:
            for key in n_num.keys():
                if n_num[key] >= 3:
                    # print("cslnb")
                    pass
                    solved = True
                    break

            ind_pairs = []
            if not solved:
                for key in n_num.keys():
                    if n_num[key] == 2:
                        ind_pairs.append(key)

                if len(ind_pairs) >= 2:
                    # print("cslnb")
                    pass
                    solved = True
                elif len(ind_pairs) == 1 and (ind_pairs[0] - 1) in n_num:
                    # print("cslnb")
                    pass
                    solved = True

                else:
                    sum_targ = n * (n - 1) // 2
                    dif_sum = s - sum_targ
                    if dif_sum % 2 == 0:
                        # print("cslnb")
                        pass

                    else:
                        # print("sjfnb")
                        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)