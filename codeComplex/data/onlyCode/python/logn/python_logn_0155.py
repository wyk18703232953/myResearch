
def sm(n):
    return int(int(n*(n+1))/int(2));
def summ(en, st):
    if(st <= 1):
        return sm(en);
    return sm(en) - sm(st-1);

def bs(n, k):
    st = 1;
    en = k;
    while (st < en):
        md = int(int((st+en)) /int(2));
        s = summ(k,md);
        if(s == n):
            return k - md + 1;
        elif (s>n):
            st = md + 1;
        else :
            en = md;
    return k - st + 2;
n, k = input().split();
n = int(n);
k = int(k);

if(n == 1):
    print(0);
elif (n <= k):
    print(1);
else:
    n -= 1;
    k -= 1;
    if(sm(k) < n ):
        print(-1);
    else:
        print(int(bs(n,k)));
