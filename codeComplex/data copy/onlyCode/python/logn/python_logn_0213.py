n, s = map(int, input().split())
def really_big(ni, s):
    dig_sum = sum(list(map(int, list(str(ni)))))
    return (ni-dig_sum)>=s
cont = 0
for i in range(s, n+1):
    if really_big(i, s):
        cont = n-i+1
        break
print(cont)