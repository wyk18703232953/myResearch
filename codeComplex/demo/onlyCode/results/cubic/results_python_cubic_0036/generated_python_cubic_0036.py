def main(n):
    if n <= 0:
        return 0
    st = ''.join(chr(ord('a') + (i % 3)) for i in range(n))
    m = 0
    length = len(st)
    for i in range(length):
        for j in range(i, length + 1):
            if st[i:j] in st[i + 1:length] and len(st[i:j]) > m:
                m = len(st[i:j])
    return m

if __name__ == "__main__":
    print(main(10))