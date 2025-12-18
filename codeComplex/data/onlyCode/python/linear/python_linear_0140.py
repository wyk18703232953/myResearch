'''
mark-up-1 :hmmge:
'''


def f(ar):
	mx = ar.index(max(ar))
	cmark = 0
	ans = 0
	big = [0] * (len(ar))
	for i in range(len(ar) - 1, -1, -1):
		# big man nearest chote ko bharo
		cmark = max(cmark - 1, ar[i] + 1, 0)
		big[i] = cmark
	cmark = 0
	t=[0]*(len(ar))
	for i in range(len(ar)):
		cmark = max(cmark, big[i]) 
		t[i]=cmark  # total marks at that index
	ans=0
	for i in range(len(ar)):
		t[i]=t[i]-ar[i]-1 #answer calc
	return (sum(t))


a = input()
print(f([*map(int, input().strip().split())]))
