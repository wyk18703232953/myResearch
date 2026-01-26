a,b,c = input().split()
if a[1] == b[1] == c[1]:
    t = sorted([int(a[0]),int(b[0]),int(c[0])])
    if (t[1] == t[0] + 1 == t[2] - 1) or (t[0] == t[2]):print(0)
    elif t[0] == t[1] or t[1] == t[2]:print(1)
    elif t[0] + 1 == t[1] or t[1] + 1 == t[2] or t[0] + 2 == t[1] or t[1] + 2 == t[2]:print(1)
    else:print(2)
elif a[1] == b[1]:
    s,t = int(a[0]),int(b[0])
    if s == t:print(1)
    elif min(s,t) + 1 == max(s,t) or min(s,t) + 2 == max(s,t):print(1)
    else:print(2)
elif c[1] == b[1]:
    s,t = int(c[0]),int(b[0])
    if s == t:print(1)
    elif min(s,t) + 1 == max(s,t) or min(s,t) + 2 == max(s,t):print(1)
    else:print(2)
elif a[1] == c[1]:
    s,t = int(a[0]),int(c[0])
    if s == t:print(1)
    elif min(s,t) + 1 == max(s,t) or min(s,t) + 2 == max(s,t):print(1)
    else:print(2)
else:print(2)
