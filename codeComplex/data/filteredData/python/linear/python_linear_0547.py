def main(n):
    # Deterministically generate input array 'a' of length n
    # Example pattern ensures varied values, including potential gaps
    a = [(i * 2) % (n + 3) for i in range(n)]

    mex = -1
    for i in range(n):
        if a[i] <= mex:
            continue
        elif a[i] == mex + 1:
            mex += 1

        else:
            # print(i + 1)
            pass
            return
    # print(-1)
    pass
if __name__ == "__main__":
    main(10)