def main(n):
    # Deterministic data generation
    # Map n to length of string c and parameter b
    # Let length of c be n, and b be n//2 (at least 1)
    length_c = max(1, n)
    b = max(1, n // 2)

    # Generate c as first length_c letters repeating over abc
    abc = "abcdefghijklmnopqrstuvwxyz"
    c_chars = [abc[i % 26] for i in range(length_c)]
    c = "".join(c_chars)

    # Core logic from original program
    summa = 0
    count = 0
    j = -2
    i = 0
    while i < 26 and count < b:
        if abc[i] in c and i - 2 >= j:
            summa += i + 1
            count += 1
            j = i
        i += 1

    if count < b:
        result = -1

    else:
        result = summa

    # print(result)
    pass
if __name__ == "__main__":
    main(10)