from queue import Queue
import datetime

with open("input.txt", 'r') as in_file:
    n, m = (int(i) for i in in_file.readline().split(" "))
    k = int(in_file.readline())
    ints = [int(i) for i in in_file.readline().split(" ")]

pairs = []
for i in range(0, len(ints), 2):
    x = ints[i]
    y = ints[i+1]
    pairs.append((x, y))


last_tree = (1, 1)
maxd = 0
mult = m * n
for i in range(1, n+1):
    for j in range(1, m+1):
        md = mult
        # print("par", i, j)
        for pair in pairs:
            x, y = pair
            d = abs(i-x)+abs(j-y)
            # print("punto", x, y)
            # print("distancia", d)
            md = min(md, d)
            # print("min", md)
        if md > maxd:
            # print("max", md)
            last_tree = (i, j)
            maxd = md
        # print("")

# print("res", last_tree)
with open("output.txt", 'w') as out_file:
    out_file.write(f"{last_tree[0]} {last_tree[1]}")

	 		 	 			  		 		         		  	