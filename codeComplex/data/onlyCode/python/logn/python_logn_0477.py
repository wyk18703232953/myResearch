'''input

'''
def solve():
	c,d = 0,0
	print("?",c,d,flush=True)
	ans = int(input())
	if ans==0:
		#both the numbers are equal 
		num = 0 
		for i in range(29,-1,-1):
			c = 1<<i
			d = 0
			print("?",c,d,flush=True)
			ans =int(input())
			if ans ==-2:
				return
			if ans == -1:
				num+=(1<<i)
		print("!",num,num)
	else:
		l = [0,0]
		if ans == 1:
			cur = 0 
		else:
			cur = 1

		prev = ans
		#first find set of mutually exclusive bits
		for i in range(29,-1,-1):
			tc = c|(1<<i)
			td = d|(1<<i)
			print("?",tc,td,flush=True)
			ans = int(input())
			if ans ==-2:
				return
			if ans ==0:
				break
			if ans !=prev:
				l[cur] += (1<<i)
				if cur ==0:
					c = tc
				else:
					d = td
				print("?",c,d,flush=True)
				temp = int(input())
				prev = temp
				if temp == 1:
					cur = 0
				else:
					cur = 1
		c = l[0]
		d = l[1]
		# now try to find common bits
		for i in range(29,-1,-1):
			if c&(1<<i) != 0 or d&(1<<i) !=0 :
				continue
			tc = c|(1<<i)
			print("?",tc,d,flush=True)
			ans = int(input())
			if ans==-2:
				return
			if ans==-1:
				l[0]|=(1<<i)
				l[1]|=(1<<i)
		print("!",l[0],l[1])
	return 

t = 1
# t = int(input())
while t>0:
	t-=1
	solve()