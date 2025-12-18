def sum_from1(k):
      return (k*(k+1))//2
def sum_of_subtraction(p,k):
      if p<=1:
            return sum_from1(k)
      else:
            return sum_from1(k)-sum_from1(p-1)
n,k=map(int,input().split())
if n==1:
      print(0)
elif n<=k:
      print(1)
else:
      n-=1
      k-=1
      if n>sum_from1(k):
            print(-1)
      else:
            s=1
            e=k
            
            while s<e:
                  mid=(s+e)//2
                  r=sum_of_subtraction(mid,k)
                  
                  if r==n:
                        print(k-mid+1)
                        break
                  elif r>n:
                        s=mid+1
                  else:
                        e=mid
            else:
                  print(k-s+2)
 

