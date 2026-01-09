def main(n):
    if n < 0:
        n = 0
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    for i in range(len(s), 0, -1):
        if s[:i] != s[i-1::-1]:
            # print(i)
            pass
            break

    else:
        # print(0)
        pass
if __name__ == "__main__":
    main(10)