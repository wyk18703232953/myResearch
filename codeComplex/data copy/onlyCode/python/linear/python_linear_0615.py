
def main():
    n = int(input())
    a = list(map(lambda x: int(x), input().split(" ")))
    b = list(map(lambda x: int(x), input().split(" ")))
    now = 0
    ans = []
    h = set()
    for i in range(n):
        count = 0
        while b[i] not in h:
            h.add(a[now])
            now += 1
            count += 1
        ans.append(str(count))
    print(" ".join(ans))


if __name__ == '__main__':
    main()
