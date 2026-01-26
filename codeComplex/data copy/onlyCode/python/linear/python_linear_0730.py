n, k = map(int, input().split())

strr = ""
while len(strr) < n:
    strr += "0" * ((n-k) // 2) + "1"
strr = strr[:n]
print(strr)