
def check(mid,n,m,arr):
	masks = {}
	for index in range(n):
		array = arr[index]
		x = 0
		for i in range(m):
			if array[i] >= mid:
				x ^= (1<<i)
		masks[x] = index+1
	ans = False
	a,b = 1,1
	if (1<<m)-1 in masks.keys():
		return True,(masks[(1<<m)-1],masks[(1<<m)-1])
	for i in  masks.keys():
		for j in masks.keys():
			orAns = i|j
			if(orAns == ((1<<m)-1)):
				if i == (1<<m)-1 and (i in masks.keys()):
					a = masks[i]
					ans = True
					break
				elif j == (1<<m)-1 and (j in masks.keys()):
					b =  masks[j]
					ans = True
					break
				elif (i in masks.keys()) and (j in masks.keys()):
					ans = True
					a,b = masks[i],masks[j]
					break
	return ans,(a,b)

def solve(n,m,arr):
	mini = 0
	maxi = int(1e9)+5
	i,j = 1,1
	while(mini<=maxi):
		mid = (mini+maxi)//2
		ans,res = check(mid,n,m,arr)
		if(ans):
			i,j = res
			mini =mid +1
		else:
			maxi = mid -1
	print(i,j)

def main():
	n,m = map(int,input().split(' '))
	arr = []
	for _ in range(n):
		x = list(map(int,input().split(' ')))
		arr.append(x)
	solve(n,m,arr)

main()