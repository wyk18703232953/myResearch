n = int

def main(n):
    a = [i // 2 for i in range(n)]
    mex = -1
    for i in range(n):
        if a[i] <= mex:
            continue
        elif a[i] == mex + 1:
            mex += 1
        else:
            print(i + 1)
            return
    print(-1)

if __name__ == "__main__":
    main(10)