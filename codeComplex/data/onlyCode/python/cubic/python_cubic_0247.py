

def read_int():
    return int(raw_input().strip())


def read_ints():
    return list(map(int, raw_input().strip().split(' ')))


def solve():
    '''
    8 8 8 8 8 8
    9 9
    9 9

    81+81

    72+72+72+72
    '''
    R, G, B = read_ints()
    dp = [[[0 for _ in range(B+1)] for _ in range(G+1)] for _ in range(R+1)]
    # dp[R][G][B]
    Rs = read_ints()
    Gs = read_ints()
    Bs = read_ints()
    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)
    answer = 0
    for r in range(R+1):
        for g in range(G+1):
            for b in range(B+1):
                if r > 0 and g > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r-1][g-1][b]+Rs[r-1]*Gs[g-1])
                if g > 0 and b > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r][g-1][b-1]+Gs[g-1]*Bs[b-1])
                if r > 0 and b > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r-1][g][b-1]+Rs[r-1]*Bs[b-1])
                answer = max(answer, dp[r][g][b])
    return answer


if __name__ == '__main__':
    print(solve())
