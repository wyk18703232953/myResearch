def main(n):
    k = [i % 5 + 1 for i in range(n)]
    k.sort()
    k = tuple(k)

    ans = [(2, 4, 4), (3, 3, 3)]
    if k.count(1) >= 1:
        # print("YES")
        pass
    elif k.count(2) >= 2:
        # print("YES")
        pass
    elif k.count(3) >= 3:
        # print("YES")
        pass
    elif k in ans:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(5)