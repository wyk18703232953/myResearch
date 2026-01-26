def main(n):
    # n: length of the generated list a
    # deterministically generate input array a of size n
    a = [i % 5 for i in range(n)]

    q = (10 ** 6) * [-1]
    pnt = -1
    ans = "YES"
    for i in range(n):
        if pnt == -1:
            pnt += 1
            q[pnt] = a[i]

        else:
            if q[pnt] == a[i] or abs(q[pnt] - a[i]) % 2 == 0:
                q[pnt] = -1
                pnt -= 1

            else:
                pnt += 1
                q[pnt] = a[i]
    if pnt > 0:
        ans = "NO"
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)