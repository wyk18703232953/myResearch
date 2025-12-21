def main(n):
    k = n
    if k <= 9:
        return k
    else:
        s = 9
        d = 1
        prev_s = s
        while s < k:
            d += 1
            prev_s = s
            s += (10**d - 10**(d-1)) * d
        digit_pos = k - (prev_s + 1)
        number = 10**(d-1) + digit_pos // d
        if digit_pos / d != digit_pos // d:
            digit_pos = digit_pos - (digit_pos // d) * d
        else:
            digit_pos = 0
        return int(str(number)[digit_pos])

if __name__ == "__main__":
    for i in range(1, 25):
        print(i, "->", main(i))