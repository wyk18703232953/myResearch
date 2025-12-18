from sys import stdin,stdout

# stdin  = open("input.txt","r")
# stdout = open("output.txt","w")


final_ans=0

# def solve(r,g,b):
# 	print(r,g,b)
# 	ans=0
# 	if min(r,g,b)<0:
# 		return 0
# 	if dparr[r-1][g-1][b]==-1:
# 		solve(r-1,g-1,b)
# 	ans=max(ans,dparr[r-1][g-1][b]+Ra[r-1]*Ga[g-1])
# 	if dparr[r-1][g][b-1]==-1:
# 		solve(r-1,g,b-1)
# 	ans=max(ans,dparr[r-1][g][b-1]+Ra[r-1]*Ba[b-1])
# 	if dparr[r][g-1][b-1]==-1:
# 		solve(r,g-1,b-1)
# 	ans=max(ans,dparr[r][g-1][b-1]+Ga[g-1]*Ba[b-1])
# 	dparr[r][g][b]=ans


R,G,B = map(int,stdin.readline().strip().split(' '))
Ra = sorted(list(map(int, stdin.readline().strip().split(' '))), reverse=True)
Ga = sorted(list(map(int, stdin.readline().strip().split(' '))), reverse=True)
Ba = sorted(list(map(int, stdin.readline().strip().split(' '))), reverse=True)

dparr=[[[-1 for i in range(B+1)] for j in range(G+1)] for k in range(R+1)]
dparr[1][1][0]=Ra[0]*Ga[0]
dparr[1][0][1]=Ra[0]*Ba[0]
dparr[0][1][1]=Ga[0]*Ba[0]
final_ans=max(final_ans,dparr[1][1][0],dparr[1][0][1],dparr[0][1][1])
# solve(R,G,B)
# stdout.write(str(dparr[R][G][B])+"\n")


def add_ns(t1):
	global queue,Ra,Ga,Ba,dparr
	x,y,z=t1
	if x+1<=R:
		if y+1<=G:
			if dparr[x+1][y+1][z]==-1:
				queue.append((x+1,y+1,z))
				dparr[x+1][y+1][z]=0
		
		if z+1<=B:
			if dparr[x+1][y][z+1]==-1:
				queue.append((x+1,y,z+1))
				dparr[x+1][y][z+1]=0
	if y+1<=G and z+1<=B:
		if dparr[x][y+1][z+1]==-1:
			queue.append((x,y+1,z+1))
			dparr[x][y+1][z+1]=0

def store_ans(t1):
	global final_ans,dparr,Ra,Ga,Ba
	x,y,z=t1
	if dparr[x-1][y-1][z]!=-1 and min(x-1,y-1,z)>=0:
		# print(dparr[x-1][y-1][z]+Ra[x-1]*Ga[y-1])
		dparr[x][y][z] = max(dparr[x][y][z],dparr[x-1][y-1][z]+Ra[x-1]*Ga[y-1])
	if dparr[x-1][y][z-1]!=-1 and min(x-1,y,z-1)>=0:
		# print(dparr[x-1][y][z-1]+Ra[x-1]*Ba[z-1])
		dparr[x][y][z] = max(dparr[x][y][z],dparr[x-1][y][z-1]+Ra[x-1]*Ba[z-1])
	if dparr[x][y-1][z-1]!=-1 and min(x,y-1,z-1)>=0:
		# print(dparr[x][y-1][z-1]+Ga[y-1]*Ba[z-1])
		dparr[x][y][z] = max(dparr[x][y][z],dparr[x][y-1][z-1]+Ga[y-1]*Ba[z-1])
	# print(dparr[x][y][z])

	final_ans=max(final_ans,dparr[x][y][z])

queue=[(1,1,0),(1,0,1),(0,1,1)]
add_ns(queue[0])
add_ns(queue[1])
add_ns(queue[2])
ptr=3

while ptr<len(queue):
	# print(queue[ptr])
	store_ans(queue[ptr])
	# print()
	add_ns(queue[ptr])
	
	ptr+=1

stdout.write(str(final_ans)+"\n")