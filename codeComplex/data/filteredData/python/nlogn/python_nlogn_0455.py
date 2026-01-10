def main(n):
    # n controls the size of numList
    if n <= 0:
        return

    # Deterministic generation of parameters
    length = n
    targetnumber = n // 2  # deterministic target

    # Generate a deterministic list of integers
    # Example pattern: sequence with varying values around targetnumber
    numList = [(i * 3) % (n + 3) for i in range(length)]

    # Ensure targetnumber exists in numList deterministically
    # Place it at a deterministic position (e.g., middle or 0 if short)
    pos = length // 2
    if length > 0:
        numList[pos] = targetnumber

    # Core algorithm preserved
    L1 = [length, targetnumber]

    length = L1[0]
    targetnumber = L1[1]
    pos = numList.index(targetnumber)
    pos_r = pos + 1
    rem = 0
    right = {0: 1}
    left = {0: 1}
    while pos_r <= length - 1:
        if numList[pos_r] > targetnumber:
            rem += 1
        else:
            rem -= 1
        if rem not in right:
            right[rem] = 1
        else:
            right[rem] += 1
        pos_r += 1
    pos_l = pos - 1
    rem = 0
    while pos_l >= 0:
        if numList[pos_l] > targetnumber:
            rem += 1
        else:
            rem -= 1
        if rem not in left:
            left[rem] = 1
        else:
            left[rem] += 1
        pos_l -= 1
    total = 0
    for number_l in left:
        if -number_l in right:
            total += left[number_l] * right[-number_l]
        if 1 - number_l in right:
            total += left[number_l] * right[1 - number_l]
    print(total)


if __name__ == "__main__":
    main(10)