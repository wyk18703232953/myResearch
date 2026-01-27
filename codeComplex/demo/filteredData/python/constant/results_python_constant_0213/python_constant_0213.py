def main(n):
    k1 = n
    k2 = n % 5 + 1
    k3 = (2 * n) % 7 + 1
    l = [k1, k2, k3]
    if min(k1, k2, k3) == 1:
        # print('yes')
        pass
    elif l.count(2) >= 2:
        # print('yes')
        pass
    elif l.count(3) == 3:
        # print('yes')
        pass
    elif l.count(4) == 2 and l.count(2) == 1:
        # print('yes')
        pass

    else:
        # print('no')
        pass
if __name__ == "__main__":
    main(10)