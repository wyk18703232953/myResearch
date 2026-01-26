def main(n):
    # Deterministic generation of inputs a and b based on n
    # a: string of digits of length n (repeating "0123456789")
    # b: string of digits of length n (repeating "9876543210")
    if n <= 0:
        return
    digits_a = "0123456789"
    digits_b = "9876543210"
    a = "".join(digits_a[i % 10] for i in range(n))
    b = "".join(digits_b[i % 10] for i in range(n))

    v = sorted(a)
    v = v[::-1]
    x = ""
    for i in range(len(v)):
        x = x + v[i]
    v = x
    if len(a) < len(b):
        # print(v)
        pass

    else:
        if b == a:
            # print(a)
            pass

        else:
            fin = ""
            flag = False
            for j in range(len(a)):
                for k in range(len(a)):
                    num = fin + v[k] + ''.join(sorted(v[:k] + v[k+1:]))
                    if num <= b:
                        fin += v[k]
                        if int(v[k]) < int(b[j]):
                            flag = True
                            v = v[:k] + v[k+1:]
                            fin += v
                        v = v[:k] + v[k+1:]
                        break
                if flag:
                    break
            # print(fin)
            pass
if __name__ == "__main__":
    main(10)