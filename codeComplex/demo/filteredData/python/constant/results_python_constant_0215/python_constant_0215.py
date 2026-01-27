def main(n):
    k1 = n
    k2 = n + 1
    k3 = n + 2
    l = [k1, k2, k3]
    if 1 in l:
        # print("YES")
        pass
    elif l.count(2) >= 2:
        # print("YES")
        pass
    elif l.count(3) == 3:
        # print("YES")
        pass
    elif sorted(l) == [2, 4, 4]:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(3)