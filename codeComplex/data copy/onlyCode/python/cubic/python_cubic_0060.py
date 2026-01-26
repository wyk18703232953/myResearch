name = input()
for i in range(len(name), 0, -1):
	for j in range(len(name) - i + 1):
		if name[j: j + i] in name[j + 1:]:
			print(i)
			exit()
print(0)
  				  	 	 	 			 			 			 	