def bigNumber(n, s):
  for i in range(s, n + 1):
    sumVal = 0
    num = i
    while num:
      sumVal += num % 10
      num //= 10
    if i - sumVal >= s:
      print(n - i + 1)
      return
  print(0)

n, s = (int(x) for x in input().split())
bigNumber(n,s)
  	   		   		   						   		