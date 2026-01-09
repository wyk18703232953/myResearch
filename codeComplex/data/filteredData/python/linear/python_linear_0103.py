def main(n):
    a = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    b = ''.join(chr(ord('z') - (i % 26)) for i in range(n))
    p = []
    for i in range(len(a)):
        for j in range(len(b)):
            ok = a[:i+1] + b[:j+1]
            p.append(ok)
    if p:
        # print(min(p))
        pass

    else:
        # print("")
        pass
if __name__ == "__main__":
    main(5)