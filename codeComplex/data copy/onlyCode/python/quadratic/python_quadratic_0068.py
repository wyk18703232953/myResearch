def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                cnt += 1
    even = cnt % 2 == 0
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        len = r - l + 1
        pairs = len * (len-1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            print('even')
        else:
            print('odd')


main()