def main(n):
    # Generate deterministic strings s1 and s2 based on n
    # s1 length = n, s2 length = n
    s1 = "".join(chr(ord('a') + (i % 26)) for i in range(n))
    s2 = "".join(chr(ord('z') - (i % 26)) for i in range(n))

    output = s1 + s2
    for j in range(len(s1)):
        s = s1[:j + 1]
        for k in range(len(s2)):
            s += s2[k]
            if sorted([s, output])[0] == s:
                output = s
    # print(output)
    pass
if __name__ == "__main__":
    main(10)