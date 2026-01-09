def main(n):
    # Interpret n as the number of elements in the list, k is fixed relative to n
    if n <= 0:
        return
    # Choose a deterministic k based on n, ensuring k >= 1 and reasonably scaled
    k = max(1, n // 4 + 1)

    # Generate deterministic input list ls of length n, elements in [0, 255]
    # Use a simple arithmetic pattern to keep values within 0..255
    ls = [(i * 37 + 13) % 256 for i in range(n)]

    ar = [-1 for _ in range(256)]

    outputs = []
    for e in ls:
        if ar[e] == -1:
            tmp = max(0, e - k + 1)
            i = tmp
            while i <= e:
                if ar[i] != -1 and ar[i] != i:
                    tmp += 1
                    i += 1
                    continue

                else:
                    while i <= e:
                        ar[i] = tmp
                        i += 1
        outputs.append(str(ar[e]))
    # print(" ".join(outputs))
    pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(1000)