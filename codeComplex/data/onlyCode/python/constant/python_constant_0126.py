s = input()
if int(s) < 0:
    k = int(s)/10
    m = s[:len(s)-2]+s[-1]
    print(max(int(k),int(m)))

else:
    print(s)