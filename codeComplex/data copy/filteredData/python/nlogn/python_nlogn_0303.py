def main(n):
    # Generate deterministic data based on n

    # Generate array of length n: arr_values
    # Example: arr[i] = (i * 2 + 3) % (n + 7)
    arr_values = [((i * 2 + 3) % (n + 7)) for i in range(n)]

    # Generate a deterministic string of length n containing '0' and '1'
    # Example pattern: '0' if i % 3 != 0 else '1'
    s = ''.join('0' if i % 3 != 0 else '1' for i in range(n))

    # Rebuild the original logic using generated data
    arr = list(enumerate(arr_values))
    arr.sort(key=lambda x: x[1])

    i = 0
    brr = []
    output = []

    for j in s:
        if j == "0":
            brr.append(arr[i])
            output.append(str(arr[i][0] + 1))
            i += 1

        else:
            x = brr.pop()
            output.append(str(x[0] + 1))

    # Print all outputs in one line, space-separated
    # print(" ".join(output))
    pass
if __name__ == "__main__":
    main(10)