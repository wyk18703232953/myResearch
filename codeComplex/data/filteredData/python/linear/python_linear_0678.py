def main(n):
    # deterministically generate input array a of length n
    a = [(i * 2 + 1) for i in range(n)]
    st = [a[0]]
    for i in range(1, n):
        if len(st) > 0 and st[-1] % 2 == a[i] % 2:
            st.pop()

        else:
            st.append(a[i])
    if len(st) <= 1:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)