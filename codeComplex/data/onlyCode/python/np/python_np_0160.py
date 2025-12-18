n,l,r,x = map(int,input().split())
nums = sorted(list(map(int,input().split())))
ans = 0
def recurse(i,sum, dif, cnt):
    global ans
    if i == n:
        if not cnt:
            return
        if sum>=l and sum <= r and abs(cnt[-1]-cnt[0]) >=x:
            ans += 1
        return
    recurse(i+1,sum,dif,cnt[:])
    cnt.append(nums[i])
    recurse(i+1,sum+nums[i],dif,cnt[:])
recurse(0,0,0,[])
print(ans)