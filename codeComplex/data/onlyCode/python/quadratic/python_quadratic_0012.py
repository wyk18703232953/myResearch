#Collaborated with no one
#Problem C

ans = []
import math
disks_rad = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]
r = disks_rad[1]
ans.append(r)
for i in range(1, disks_rad[0]):
  y_cord = r
  for j in range(i):
      if ((nums[i] - nums[j]) ** 2) <= ((r ** 2) * 4):
          y_cord = max(y_cord,
                        ans[j] +
                        math.sqrt(4 *
                                  (r ** 2) -
                                  (nums[j] - nums[i]) ** 2
                                )
                      )
  ans.append(y_cord)
print(" ".join([str(x) for x in ans]))
	 		    								  	  		  		 			