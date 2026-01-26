n, m = map(int, input().split())
s = input()
t = input()
if "*" in s:
    front, back = s.split("*")
    if len(t) >= len(s) - 1 and t.startswith(front) and t.endswith(back):
        print("YES")
    else:
        print("NO")
else:
    print("YES" if s == t else "NO")
