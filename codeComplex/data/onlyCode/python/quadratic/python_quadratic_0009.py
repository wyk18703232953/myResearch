#Problem Set C: Collaborated with no one

import math

n_r = list(map(int, input().split()))

n = n_r[0]
radii = n_r[1]

x_list = list(map(int, input().split()))

temp_arr = []
for i in range(n):
    temp_arr.append(max([radii] + [math.sqrt(4*radii**2 - (x_list[i]-x_list[j])**2) + temp_arr[j]
                    for j in range(i) if abs(x_list[i]-x_list[j]) <= 2*radii])
                    )

for i in temp_arr:
    print(i, end= " ")
      						 	     			   	   		