def main(n):
    # Generate a deterministic binary string s of length n
    # Pattern: alternating '1' and '0', starting with '1'
    s = ''.join('1' if i % 2 == 0 else '0' for i in range(n))

    # Core logic preserved from original program
    result = '1' * min(s.count('1'), 1) + '0' * s.count('0')
    # print(result)
    pass
if __name__ == "__main__":
    main(10)