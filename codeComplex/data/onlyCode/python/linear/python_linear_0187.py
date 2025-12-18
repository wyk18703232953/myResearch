import math

input()
all_days_problems = list(map(int, input().split()))
sum_count = sum(all_days_problems)
half_problems = math.ceil(sum_count/2)
current_sum = 0
answer = 0
for num in all_days_problems:
    answer += 1
    current_sum +=num
    if current_sum >=half_problems:
        break

print(answer)
 	   	 	 	 								 	  		 	   	