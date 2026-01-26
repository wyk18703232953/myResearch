def candy_eaten(n, k):

    choco = 1
    last = 1
    eat = 0
    # for i in range(n - 1):
    i = n - 1
    while i > 0:
        if choco > k:
            temp = choco - k
            choco -= temp
            eat += temp
            i -= temp
        else:
            last += 1
            choco += last
            i -= 1
    return eat


if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    print(candy_eaten(n, k))
