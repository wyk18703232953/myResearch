def is_pal(s):
    if s == s[::-1]:
        return True

    else:
        return False

def main(n):
    if n <= 0:
        s = ""

    else:
        s = "".join(chr(ord('a') + (i % 3)) for i in range(n))

    if not is_pal(s):
        # print(len(s))
        pass

    else:
        not_eq = False
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                # print(len(s)-1)
                pass
                not_eq = True
                break
        if not not_eq:
            # print(0)
            pass
if __name__ == "__main__":
    main(10)