def main(n):
    left = 0
    right = n
    if left == right:
        return 0
    else:
        x = 1
        while x <= right:
            x *= 2
        x //= 2
        y = x
        while (y > 0 and x <= left) or x > right:
            if x <= left:
                x += y
            else:
                x -= y
            y //= 2
        return x ^ (x - 1)

if __name__ == "__main__":
    print(main(10))