def main(n):
    l = n
    r = n * 2
    r1 = len(bin(r)) - 3
    l1 = len(bin(l)) - 3
    ans = 0
    while l > 0:
        if l1 == r1:
            r -= (1 << l1)
            l -= (1 << l1)
        else:
            ans = (1 << (r1 + 1)) - 1
            break
        z1 = min(l, r)
        z2 = max(l, r)
        l, r = z1, z2
        r1 = len(bin(r)) - 3
        l1 = len(bin(l)) - 3
    if ans == 0:
        if l1 == r1:
            if r == 1:
                return 1
            else:
                return 0
        else:
            return (1 << (r1 + 1)) - 1
    else:
        return ans

if __name__ == "__main__":
    print(main(10))