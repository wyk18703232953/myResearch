def main(n):
    # Generate two deterministic binary strings of length n
    # Pattern: '0' and '1' alternating with slight phase shift between arr1 and arr2
    arr1_str = ''.join('0' if i % 2 == 0 else '1' for i in range(n))
    arr2_str = ''.join('0' if (i + 1) % 3 == 0 else '1' for i in range(n))

    arr1 = bytearray(arr1_str.encode())
    arr2 = bytearray(arr2_str.encode())

    length, tot = len(arr1), 0
    for i in range(length - 1):
        if arr1[i] == 48 and arr1[i + 1] == 48 and arr2[i] == 48:
            tot += 1
            arr1[i] = 49
            arr1[i + 1] = 49
            arr2[i] = 49
        elif arr1[i] == 48 and arr2[i] == 48 and arr2[i + 1] == 48:
            tot += 1
            arr1[i] = 49
            arr2[i] = 49
            arr2[i + 1] = 49
        elif arr2[i] == 48 and arr2[i + 1] == 48 and arr1[i + 1] == 48:
            tot += 1
            arr2[i] = 49
            arr2[i + 1] = 49
            arr1[i + 1] = 49
        elif arr1[i] == 48 and arr1[i + 1] == 48 and arr2[i + 1] == 48:
            tot += 1
            arr1[i] = 49
            arr1[i + 1] = 49
            arr2[i + 1] = 49

    # print(tot)
    pass
if __name__ == "__main__":
    main(10)