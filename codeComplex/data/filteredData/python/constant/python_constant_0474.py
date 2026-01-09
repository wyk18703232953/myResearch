def main(n):
    # Interpret n as coordinate scale, deterministically generate points
    ax = 0
    ay = 0
    bx = n
    by = n // 2
    cx = n // 2
    cy = n

    if ((bx - ax < 0 and cx - ax < 0 or
         bx - ax > 0 and cx - ax > 0) and
        (by - ay < 0 and cy - ay < 0 or
         by - ay > 0 and cy - ay > 0)):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)