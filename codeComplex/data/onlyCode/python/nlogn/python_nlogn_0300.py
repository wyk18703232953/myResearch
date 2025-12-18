n = int(input())
w = list(map(int, input().split()))
intro = [[v, i] for i, v in enumerate(w, 1)]
intro.sort(key=lambda x: x[0])
s = input()
i = -1
li = []
ans = []
for j in s:
    if j == "0":
        i += 1
        ans.append(intro[i][1])
        li.append(intro[i][1])
    else:
        ans.append(li.pop(-1))
print(" ".join(map(str, ans)))

		       	   	       		 			  	