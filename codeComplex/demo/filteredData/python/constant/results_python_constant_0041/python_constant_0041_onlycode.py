n = int(input())
m = ''.join(set(list(str(n))))
if m == '47' or m == '74' or m == '4' or m == '7':
  print('YES')
else:
  if n %4 == 0 or n %7== 0 or n %74== 0 or n %47== 0:
    print('YES')
  else:
    print("NO")