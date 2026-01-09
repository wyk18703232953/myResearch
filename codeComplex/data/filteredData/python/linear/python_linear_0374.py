def main(n):
    # Generate a deterministic binary string with '0', '1', '2'
    # Pattern: cycle through '0','1','2' using i % 3
    chars = ['0', '1', '2']
    s = ''.join(chars[i % 3] for i in range(n))

    one = s.count('1')
    zero = 0
    ind = -1
    for i in range(len(s)):
        if s[i] == '2':
            ind = i
            break
        if s[i] == '0':
            zero += 1
    d = ""
    if ind == -1:
        result = "0" * zero + "1" * one
        return result
    d = d + "0" * zero + "1" * one
    for i in s[ind:]:
        if i != '1':
            d += i
    return d


if __name__ == "__main__":
    # Example call for testing / timing
    # print(main(10))
    pass