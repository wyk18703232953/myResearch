

def s(n):
    return (n*(n+1))//2

def diff(st,en):
    return s(en) - s(st-1)

def bs(k,n):
    st = 1
    en = k
    while(st < en):
        mid = (st+en)//2
        sum = diff(mid,k)
        if sum == n:
             return k-mid+1
        if sum > n:
            st = mid+1
        else:
            en = mid
    return k-st+2


if __name__ == '__main__':
   n,k = map(int,input().split())
   if n == 1:
       print(0)
   elif n <= k:
       print(1)
   else:
       n-=1
       k-=1
       if s(k) < n:
            print(-1)
       else:
           print(bs(k,n))








