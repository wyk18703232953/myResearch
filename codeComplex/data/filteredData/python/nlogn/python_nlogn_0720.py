def main(n):
	a=[[],[],[]]
	colors = ['m', 'p', 's']
	tiles = []
	for i in range(n):
		num = (i % 9) + 1
		color = colors[(i // 9) % 3]
		tiles.append(str(num) + color)
	for t in tiles:
		if t[1] == 'm':
			a[0].append(int(t[0]))
		elif t[1] == 'p':
			a[1].append(int(t[0]))
		else:
			a[2].append(int(t[0]))
	ko=10
	for i in range(len(a)):
		a[i]=sorted(a[i])
		c=0
		for j in range(1,len(a[i])):
			if(a[i][j]==a[i][j-1]):
				c+=1
		if(c==1):
			ko=min(ko,1)
		elif(c==2):
			ko=min(ko,0)
		else:
			if(len(a[i])>0):
				ko=min(ko,2)
	ans=ko
	ko=10
	for i in range(len(a)):
		a[i]=sorted(a[i])
		c=0
		for j in range(1,len(a[i])):
			if(a[i][j]==a[i][j-1]+1):
				c+=1
		if(c==1):
			ko=min(ko,1)
		elif(c==2):
			ko=min(ko,0)
		elif(len(a[i])>1 and (a[i][0]+2==a[i][1])):
			ko=min(ko,1)
		elif(len(a[i])>2 and (a[i][1]+2==a[i][2])):
			ko=min(ko,1)
		else:
			if(len(a[i])>0):
				ko=min(ko,2)
	print(min(ans,ko))

if __name__ == "__main__":
	main(20)