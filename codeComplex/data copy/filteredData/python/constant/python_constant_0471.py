def main(n):
    # Deterministically generate points based on n
    ax = n
    ay = n * 2
    bx = n // 2
    by = n * 3
    cx = n * 2
    cy = n // 3 if n != 0 else 0

    if (ax - bx) * (ax - cx) > 0 and (ay - by) * (ay - cy) > 0:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)