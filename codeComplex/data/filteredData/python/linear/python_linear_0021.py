def judge(x):
    if x % 2 == 0:
        return 0

    else:
        return 1

def main(n):
    if n < 3:
        n = 3
    ls = [(i % 4) for i in range(1, n + 1)]
    if judge(ls[0]) == judge(ls[1]):
        for x in ls[2:]:
            if judge(x) != judge(ls[0]):
                # print(ls.index(x) + 1)
                pass
                break

    else:
        if judge(ls[2]) == judge(ls[0]):
            # print(2)
            pass
        elif judge(ls[2]) == judge(ls[1]):
            # print(1)
            pass
if __name__ == "__main__":
    main(10)