def main(n):
    # Interpret n as coordinate scale; generate deterministic positions
    ax = n // 4 + 1
    ay = n // 4 + 1
    bx = n // 2 + 1
    by = n // 3 + 1
    cx = n - bx
    cy = n - by

    if bx < ax < cx or bx > ax > cx or by < ay < cy or cy < ay < by:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
if __name__ == "__main__":
    main(10)