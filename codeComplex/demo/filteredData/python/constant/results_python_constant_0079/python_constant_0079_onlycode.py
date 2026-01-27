def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

if __name__ == "__main__":
    n = int(input())
    ans = 0
    if n==1:
        ans = 1
    elif n==2:
        ans = 2
    else:
        if n%2!=0:
            ans = n*(n-1)*(n-2)
        else:
            if gcd(n,(n-3)) ==1:
                ans = n*(n-1)*(n-3)
            else:
                ans = (n-1)*(n-2)*(n-3)
    print(ans)