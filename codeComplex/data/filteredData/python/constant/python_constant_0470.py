def main(n):
    # Generate deterministic test data based on n
    # queen, king, target are 2D coordinates
    # Make coordinates grow roughly with n to scale input "size"
    queen = [n, 2 * n]
    king = [n // 2, (3 * n) // 2]
    target = [(2 * n) // 3, (5 * n) // 3]

    def done():
        # print("NO")
        pass
        return False

    def complete():
        # print("YES")
        pass
        return True

    # Core logic from original code
    if king[0] < queen[0]:
        if target[0] > queen[0]:
            return done()
        if king[1] > queen[1]:
            if target[1] < queen[1]:
                return done()
            return complete()

        else:
            if target[1] > queen[1]:
                return done()
            return complete()

    else:
        if target[0] < queen[0]:
            return done()
        if king[1] > queen[1]:
            if target[1] < queen[1]:
                return done()
            return complete()

        else:
            if target[1] > queen[1]:
                return done()
            return complete()


if __name__ == "__main__":
    main(10)