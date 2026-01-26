def main():
	n, pos, l, r=tuple(map(int,input().split()))
	time=0
	if l!=1 and r!=n:
		if abs(pos-l)<abs(pos-r):
			time+=abs(pos-l)+abs(l-r)+2
		else:
			time+=abs(pos-r)+abs(l-r)+2
	elif l==1 and r!=n:
		time+=abs(pos-r)+1
	elif r==n and l!=1:
		time+=abs(pos-l)+1
	else:
		time+=0
	print(time)
if __name__=='__main__':
	main()