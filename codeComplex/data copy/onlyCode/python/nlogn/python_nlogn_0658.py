n = int(input())
A = [0] + list(map(int,input().split()))

vec = []
for i in range(1, n+1) :
	vec = vec + [[A[i], i]]
list.sort(vec)
list.reverse(vec)
# print(vec)

if vec[0][0] == 1 :
	print("NO")
	exit(0)

dia = 0
path = [vec[0][1]]
ans = []
bol, col, idx = 1, 1, 0
for i in vec[1:] :
	# print(i)
	if i[0] != 1 :
		ans = ans + [[path[-1], i[1]]]
		dia = dia+1
		A[path[-1]] = A[path[-1]]-1
		path += [i[1]];
		A[path[-1]] = A[path[-1]]-1
	else :
		if col == 1:
			dia = dia+1
			col = 0
			A[path[0]] -= 1
			ans = ans+ [[path[0], i[1]]]
		elif bol == 1:
			dia = dia+1
			bol = 0
			A[path[-1]] -= 1
			ans = ans + [[path[-1], i[1]]]
		else :
			while idx < len(path) and A[path[idx]] == 0 :
				idx = idx+1
			if idx == len(path) :
				print("NO")
				exit(0)
			A[path[idx]] = A[path[idx]] - 1;
			ans = ans + [[path[idx], i[1]]]

print("YES", dia)
print(len(ans))
for i in ans :
	print(i[0], i[1])





