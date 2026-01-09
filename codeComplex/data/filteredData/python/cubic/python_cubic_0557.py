a=sorted("123456789")

def main(n):
    b = n
    a_local = a[::-1]
    p = ""
    while a_local:
        for i, z in enumerate(a_local):
            candidate = p + a_local[i] + "".join(sorted(a_local[:i] + a_local[i+1:]))
            if int(candidate) <= b:
                p += z
                a_local.pop(i)
                break
    # print(p)
    pass
if __name__ == "__main__":
    main(1000)