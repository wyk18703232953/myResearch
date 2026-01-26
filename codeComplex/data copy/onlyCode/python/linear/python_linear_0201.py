n, s = map(int, input().split())
times = []
result = 0 
need = True 
for i in range (n):
    h, m = map(int, input().split())
    times.append(60*h + m)

if n == 1:
    if 0 + s + 1 <= times[0]:
        need = False
for i in range(n-1):
    if 0 + s + 1 <= times[0]:
        need = False
        break
    if times[i+1] - times[i] >= 2 + 2*s:
        result = times[i] + 1 + s
        break 
if result == 0 and need:
    result = times[n-1] + 1 + s

hour = result // 60
minute = result % 60

print(hour, minute)