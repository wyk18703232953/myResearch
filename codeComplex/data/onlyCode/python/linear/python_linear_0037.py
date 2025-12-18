n, k = map(int,input().split())
arr = list(map(int, input().split()))

def find_segment(arr, n, k):
  f = [0]*100001
  L = count = 0
  R = -1
  while R < n-1:
    R += 1
    if f[arr[R]] == 0:
      count += 1
    f[arr[R]] += 1
    while count == k:
      f[arr[L]] -= 1
      if f[arr[L]] == 0:
        print(L+1, R+1)
        return
      L += 1
  print(-1,-1)
find_segment(arr, n, k)