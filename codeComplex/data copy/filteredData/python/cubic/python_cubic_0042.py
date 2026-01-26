def main(n):
    # Deterministically generate input string of length n
    # Pattern: cyclic over lowercase letters
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    length = len(s)
    ans = 0
    amap = {}

    def fun():
        nonlocal ans
        for strLen in range(length, 0, -1):
            mark = 0
            for t in range(0, length):
                if t + strLen > length:
                    break
                sub = s[t:t + strLen]
                if sub in amap:
                    amap[sub] += 1

                else:
                    amap[sub] = 1
                if amap[sub] >= 2:
                    mark = 1
                    ans = len(sub)
                    # print(ans)
                    pass
                    break
            if mark == 1:
                break

    fun()
    if ans == 0:
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)