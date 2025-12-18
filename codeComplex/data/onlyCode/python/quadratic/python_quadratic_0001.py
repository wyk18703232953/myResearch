import sys

input = sys.stdin.readline


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)

def main():
    n,r=map(int, input().split())
    a=list(map(int, input().split()))
    ans=[]
    ans.append(r)
    for i in range(1,n):
        ymax=r
        for j in range( i):
            if abs(a[j]-a[i])<=2*r:
                ymax=max(ymax, ans[j]+(4*r*r-(a[i]-a[j])**2)**0.5)
        ans.append(ymax)
    print(*ans)
    # for i in range(15):
    #     print(x[i],end=' ')













    return

if __name__=="__main__":
    main()

