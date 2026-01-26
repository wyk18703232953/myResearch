from sys import stdin, stdout
readline = stdin.readline
write = stdout.write

squareMoves = []

def precompute():
    top = 10 ** 18
    prev = 0

    while prev <= 30*top:
        squareMoves.append(prev)
        prev = 1 + 4 * prev

def getAns(k, n):
    low = 0
    high = 0
    a = 1
    b = 1
    i = 1

    while i <= n:
        low += a
        high += a + b * squareMoves[n-i]

        if high >= k:
            if low > k:
                return -1
            return i

        a = 2 * a + 1
        b = 2 * a - 1
        i += 1
    
    return -1

if __name__ == "__main__":
    precompute()

    t = int(readline().strip())
    for i in range(t):
        [n, k] = list(map(int, readline().strip().split(' ')))
        tmpN = min(n, len(squareMoves))

        ans = getAns(k, tmpN)
        if ans == -1:
            write("NO\n")
        else:
            write("YES " + str(n - ans) + "\n")
