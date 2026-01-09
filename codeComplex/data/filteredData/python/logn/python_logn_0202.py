def main(n):
    s = str(n)
    nn = str(n)
    i = int(s)
    d_sum = sum(int(ch) for ch in str(i))
    while i - d_sum < int(s):
        i += 1
        d_sum = sum(int(ch) for ch in str(i))
    result = max(0, int(nn) - i + 1)
    # print(result)
    pass
if __name__ == "__main__":
    main(10**5)