ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
if ax > bx:
    ax, bx = bx, ax
    ay, by = by, ay
if ax > cx:
    ax, cx = cx, ax
    ay, cy = cy, ay
if bx > cx:
    bx, cx = cx, bx
    by, cy = cy, by
ans = []
for i in range(min(ay, by, cy), max(ay, by, cy) + 1):
    ans.append([bx, i])
for i in range(ax, bx):
    ans.append([i, ay])
for i in range(bx + 1, cx + 1):
    ans.append([i, cy])
print(len(ans))
for x in ans:
    print(x[0], x[1])

	 	 		    		 	    	 					 	