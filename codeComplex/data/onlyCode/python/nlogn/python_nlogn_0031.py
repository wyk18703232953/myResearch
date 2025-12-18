def secondorder(arr, size):
	arr.sort()
	return arr[1]
size = int(input())
list = []
num = input().split(" ")
for i in num:
	if(int(i) not in list):
		list.append(int(i))
if len(list) == 1:
	print("NO")
else:
	print(secondorder(list, size))
 		 		 	 	 			 				    	 		   	