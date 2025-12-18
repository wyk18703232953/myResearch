import sys, os.path
if(os.path.exists('input.txt')):
	sys.stdin = open("input.txt","r")
	

t = int(input())
last = []
current = []

for i in range(t):
	last.append(str(input()))
for i in range(t):
	current.append(str(input()))

for i in range(len(last)):
	if last[i] in current:
		current[current.index(last[i])] = "*"
		last[i] = "*"

last.sort()
current.sort()

total = 0
for i in range(len(last)):
	if last[i] == current[i]:
		continue
	else:
		total+=1
	
print(total)


