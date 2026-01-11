def main(n):
    l = [i % 10 for i in range(n)]
    if l == sorted(l):
        # print("Yes")
        pass

    else:
        cnt = 0
        g = sorted(l)
        for i in range(len(l)):
            if l[i] != g[i]:
                cnt += 1
        if cnt <= 2:
            # print("Yes")
            pass

        else:
            # print("No")
            pass
if __name__ == "__main__":
    main(10)