def main(n):
    # Interpret n as the number of test cases
    test = n

    # Deterministically generate input lists
    # For test case i (0-based), generate list: [i, i+1, ..., i+i] (length i+1)
    first = []
    for i in range(test):
        list_ = [i + j for j in range(i + 1)]
        sum_ = sum(list_)
        first.append(sum_)

    if not first:
        # print(0)
        pass
        return

    first_sum = first[0]
    count = 0
    for val in first:
        if first_sum < val:
            count += 1

        else:
            continue
    # print(count + 1)
    pass
if __name__ == "__main__":
    main(10)