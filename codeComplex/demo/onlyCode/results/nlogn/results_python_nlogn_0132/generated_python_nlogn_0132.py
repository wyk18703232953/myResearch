def main(n):
    a = n
    b = n // 2 + 1
    c = 0
    arr = [i + 1 for i in range(a)]
    arr.sort()
    p = 0
    a -= 1
    while a >= 0 and c < b:
        c -= 1
        p += 1
        c += arr[a]
        a -= 1
    if c < b:
        return -1
    else:
        return p

if __name__ == "__main__":
    print(main(10))