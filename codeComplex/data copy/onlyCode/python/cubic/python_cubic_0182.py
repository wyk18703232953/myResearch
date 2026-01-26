
'''
n = input ("") # array length 
n = int(n)
the_input_string = input("")

shrinked_array = the_input_string.split(' ')

shrinked_array = [ int(num) for num in shrinked_array ]

while(1):
    done = True
    for i in range(0, len(shrinked_array)-1):
        if(shrinked_array[i] == shrinked_array[i+1]):
            done = False
            shrinked_array.pop(i+1)
            shrinked_array[i] = shrinked_array[i] + 1
            break

    if(done):
        break


print(len(shrinked_array))
'''


n = int(input())
# b = [4,3,2,2,3]
b = [int(_) for _ in input().split()]

# 2d array of array with size(n+1) and value -1
# e = [ [-1, -1, -1,-1] , [-1, -1, -1,-1] , [-1, -1, -1,-1] , [-1, -1, -1,-1], [-1, -1, -1,-1], ... (2024)  ]
e = [[-1] * (n+1) for _ in range(2024)]

# d = [ [] , [] , [] , []  ]
d = [[] for _ in range(n)]



for i, v in enumerate(b):
	e[v][i] = i
	d[i].append(i)
 
for v in range(1, 2024):
	for i in range(n):
		j = e[v][i]
		h = e[v][j+1] if j != -1 else -1
		if j != -1 and h != -1:
			e[v+1][i] = h
			d[i].append(h)
 
a = [_ for _ in range(1, n+1)]
for s in range(n):
	for e in d[s]:
		a[e] = min(a[e], a[s-1]+1 if s > 0 else 1)
print(a[n-1])