def main(n):
    # Generate a deterministic string of length n using a simple pattern
    # Pattern: 'x' at positions where i % 3 != 0 to guarantee sequences of 'x'
    s = ''.join('x' if i % 3 != 0 else 'a' for i in range(n))

    count = 0
    temp_count = 0
    for c in s:
        if c == 'x':
            temp_count += 1

        else:
            temp_count = 0
        if temp_count == 3:
            count += 1
            temp_count -= 1

    # print(count)
    pass
if __name__ == "__main__":
    main(1000)