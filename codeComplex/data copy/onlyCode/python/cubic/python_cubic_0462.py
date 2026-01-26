'''
Author: your name
Date: 2021-04-25 17:01:28
LastEditTime: 2021-04-25 17:13:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \code_py\cf_718D.py
'''


def main():
    n, m, k = map(int, input().split())
    inf = 1 << 30
    left = [list(map(int, input().split())) for i in range(n)]
    down = [list(map(int, input().split())) for i in range(n-1)]
    if k & 1:
        for i in range(n):
            print(*[-1]*m)
        exit()
    ans = [[0]*m for i in range(n)]
    for k in range(1, k//2+1):
        _ = [[inf]*m for ii in range(n)]
        for i in range(n):
            for j in range(m):
                if i:
                    _[i][j] = min(_[i][j], ans[i-1][j]+down[i-1][j])
                if i < n-1:
                    _[i][j] = min(_[i][j], ans[i+1][j]+down[i][j])
                if j:
                    _[i][j] = min(_[i][j], ans[i][j-1]+left[i][j-1])
                if j < m-1:
                    _[i][j] = min(_[i][j], ans[i][j+1]+left[i][j])
        ans = _
    for i in range(n):
        for j in range(m):
            print(ans[i][j]*2, end=' ')
        print()


if __name__ == '__main__':
    main()
