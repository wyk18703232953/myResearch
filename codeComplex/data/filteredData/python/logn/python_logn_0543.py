def main(n):
    import bisect

    xyz = [9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000, 9000000000, 900000000000]
    xzy = [10, 190, 2890, 38890, 488890, 5888890, 68888890, 788888890, 8888888890, 98888888890, 1088888888890, 11888888888890]

    # Deterministic generation of k from n
    # Map n -> k so that k grows with n but stays within representable range
    # Using a simple polynomial: k = (n + 1) * (n + 2)
    k = (n + 1) * (n + 2)

    digits = bisect.bisect_left(xzy, k)

    if k == 10:
        # print(1)
        pass
    elif k > 10:
        apu = k - xzy[digits - 1]
        modulo = apu % (digits + 1)
        dlj = apu // (digits + 1)
        output = 10 ** digits + dlj
        list1 = [i for i in str(output)]
        # print(list1[modulo])
        pass

    else:
        # print(k)
        pass
if __name__ == "__main__":
    main(1000)