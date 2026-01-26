from sys import stdin, stdout

nxt = []

def find_it(s, left, right):
    global nxt
    dp = [[1000 for i in range(len(right) + 1)] for j in range(len(left) + 1)]
    dp[0][0] = 0
    for i in range(len(left)+1):
        for j in range(len(right)+1):
            if dp[i][j] > len(s):
                continue
            if j < len(right) and nxt[ord(right[j]) - 97][dp[i][j]] != -1:
                if nxt[ord(right[j]) - 97][dp[i][j]] < dp[i][j+1]:
                    dp[i][j+1] = nxt[ord(right[j]) - 97][dp[i][j]] +1
            if i < len(left) and nxt[ord(left[i]) - 97][dp[i][j]] != - 1:
                if nxt[ord(left[i]) - 97][dp[i][j]] < dp[i+1][j]:
                    dp[i+1][j] = nxt[ord(left[i]) - 97][dp[i][j]] +1
    if dp[len(left)][len(right)] != 1000:
        return True
    else:
        return False

def main():
    global nxt
    n = int(stdin.readline())
    for _ in range(n):
        s = stdin.readline().rstrip()
        t = stdin.readline().rstrip()
        nxt = [[-1 for _ in range(len(s)+1)] for i in range(26)] 
        for i,x in enumerate(s):
            nxt[ord(x) - 97][i] = i
        for i in range(26):
            for j in range(len(s)-1 ,-1,-1):
                if nxt[i][j] != j:
                    nxt[i][j] = nxt[i][j+1]
        
        r = False            
        for i in range(len(t)):
            res = find_it(s, t[:i], t[-len(t)+i:])
            if res is True:
                r = True
                break
        
        if r is True:
            stdout.write("YES\n")
        else:
            stdout.write("NO\n")
            

main()            