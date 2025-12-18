def main():
    n = int(input())
    V = []
    for i in range(n):
        x,w = map(int,input().split())
        V.append((x-w,x+w))
    V.sort(key=lambda x: x[1])
    ans = 1
    now = V[0]
    for i in range(1,n):
        if V[i][0] >= now[1]:
            now = V[i]
            ans += 1
    print(ans)
    
if __name__ == "__main__":
    main()