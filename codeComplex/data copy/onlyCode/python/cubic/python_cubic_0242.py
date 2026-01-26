#import sys
#input = sys.stdin.readline
def main():
    R, G, B = map( int, input().split())
    Rs = list( map( int, input().split()))
    Gs = list( map( int, input().split()))
    Bs = list( map( int, input().split()))

    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)

    dp = [[[0]*(B+1) for _ in range(G+1)] for _ in range(R+1)]
    ans = 0
    for i in range(R+1):
        for j in range(G+1):
            for k in range(B+1):
                t = 0
                if i > 0 and j > 0:
                    if dp[i-1][j-1][k] + Rs[i-1]*Gs[j-1] > t:
                        t = dp[i-1][j-1][k] + Rs[i-1]*Gs[j-1]
                if j > 0 and k > 0:
                    if dp[i][j-1][k-1] + Gs[j-1]*Bs[k-1] > t:
                        t = dp[i][j-1][k-1] + Gs[j-1]*Bs[k-1]
                if k > 0 and i > 0:
                    if dp[i-1][j][k-1] + Bs[k-1]*Rs[i-1] > t:
                        t = dp[i-1][j][k-1] + Bs[k-1]*Rs[i-1]
                dp[i][j][k] = t
                if ans < t:
                    ans = t
    print(ans)
                        

if __name__ == '__main__':
    main()
