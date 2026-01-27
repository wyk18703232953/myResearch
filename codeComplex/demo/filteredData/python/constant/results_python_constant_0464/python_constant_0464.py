def main(n):
    # Deterministically generate points based on n
    # ax, ay depend on n
    ax = n
    ay = n * 2

    # bx, by and cx, cy constructed to vary relative positions with n
    bx = n // 2
    by = n // 3

    cx = n * 3
    cy = n * 4

    if bx < ax < cx:
        # print("NO")
        pass
    elif cx < ax < bx:
        # print("NO")
        pass
    elif by < ay < cy:
        # print("NO")
        pass
    elif cy < ay < by:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(10)