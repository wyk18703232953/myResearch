n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

if (bx > ax, by > ay) != (cx > ax, cy > ay):
    print("NO")
    exit(0)

print("YES")
