n,k=None,None
def main(size_n):
    global n,k
    n = size_n
    k = size_n//2
    d = (n-k)//2
    s = 0
    out_chars = []
    while s != n:
        if (s+1)%(d+1) == 0:
            out_chars.append("1")
        else:
            out_chars.append("0")
        s += 1
    result = "".join(out_chars)
    print(result)
    return result

if __name__ == "__main__":
    main(10)