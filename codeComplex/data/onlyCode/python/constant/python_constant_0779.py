import io
import os


def solve(N,):

    if N % 2 != 0:
        return "NO"
    N //= 2
    if int(N ** 0.5) ** 2 == N:
        return "YES"
    if N % 2 != 0:
        return "NO"
    N //= 2
    if int(N ** 0.5) ** 2 == N:
        return "YES"
    return "NO"


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    TC = int(input())
    for tc in range(1, TC + 1):
        (N,) = [int(x) for x in input().split()]
        ans = solve(N,)
        print(ans)
