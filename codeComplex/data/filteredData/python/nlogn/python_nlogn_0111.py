def main(n):
    lis = [i * 2 % 7 for i in range(n)]
    sor = sorted(lis)
    cnt = 0
    for i in range(n):
        if lis[i] != sor[i]:
            cnt += 1
    if cnt > 2:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main(10)