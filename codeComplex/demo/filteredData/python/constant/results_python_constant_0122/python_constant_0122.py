def main(n):
    r = str(n)
    t1 = int(r)
    if len(r) == 1:
        t2 = t1
        t3 = t1
    elif len(r) == 2:
        t2 = int(r[0])
        t3 = int(r[-1])

    else:
        t2 = int(r[:len(r)-1])
        t3 = int(r[:len(r)-2] + r[-1])
    res = max(t1, t2, t3)
    # print(res)
    pass
    return res

if __name__ == "__main__":
    main(12345)