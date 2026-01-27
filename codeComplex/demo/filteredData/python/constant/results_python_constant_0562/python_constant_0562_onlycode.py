import math

if __name__ == '__main__':
    n, m, k, l = map(int, input().split())
    one_friend = (k + l) // m + int((k + l) % m != 0)
    if one_friend * m > n:
        print(-1)
    else:
        print(one_friend)
