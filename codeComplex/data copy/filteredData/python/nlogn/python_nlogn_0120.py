def main(n):
    arr = [(i * 3 + 1) % (n + 5) for i in range(n)]
    li = arr[:]
    li.sort()
    c = 0
    for i in range(n):
        if arr[i] != li[i]:
            c += 1
        if c > 2:
            # print("NO")
            pass
            break

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(10)