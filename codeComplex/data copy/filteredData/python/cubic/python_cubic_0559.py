def main(n):
    # Deterministic data generation based on n
    # Generate string a as digits cycling 0-9, length n
    a = [str(i % 10) for i in range(n)]
    # Generate string b as digits cycling 9-0, same length as a
    b = ''.join(str(9 - (i % 10)) for i in range(n))

    a = list(a)
    out = []
    mx = '/'
    a.sort()
    a.reverse()
    x = len(a)
    if x == len(b):
        for i in range(x):
            q = 0
            for j in range(len(a)):
                if a[j] == b[i]:
                    out.append(a[j])
                    a.pop(a.index(a[j]))
                    q = 1
                    break
                elif a[j] < b[i]:
                    out.append(a[j])
                    a.pop(a.index(a[j]))
                    # print(''.join(out), end='')
                    pass
                    # print(''.join(a))
                    pass
                    return
            if q == 0:
                break
        if q == 1:
            # print(''.join(out))
            pass

        else:
            y = len(out)
            for i in range(y - 1, -1, -1):
                for j in range(len(a)):
                    if a[j] < b[i] and a[j] > mx:
                        mx = a[j]
                if mx != '/':
                    a.append(out[len(out) - 1])
                    out.pop()
                    out.append(mx)
                    a.pop(a.index(mx))
                    a.sort()
                    a.reverse()
                    # print(''.join(out), end='')
                    pass
                    # print(''.join(a))
                    pass
                    return

                else:
                    a.append(out[len(out) - 1])
                    out.pop()
                    a.sort()
                    a.reverse()
            a.pop(a.index(mx))
            # print(mx, end='')
            pass
            # print(''.join(a))
            pass

    else:
        # print(''.join(a))
        pass
if __name__ == "__main__":
    main(20)