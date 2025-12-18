from itertools import combinations
num,min_dif,max_dif,easy_hard_dif=map(int, input().split(" "))
arr=[int(m) for m in input().split(" ")]
all_combinations=[]
for x in range(2, num+1):
    combs=combinations(arr, x)
    for abc in combs:
        all_combinations.append(list(abc))
possible_answers=0
for a in all_combinations:
    if sum(a)>=min_dif and sum(a)<=max_dif and max(a)-min(a)>=easy_hard_dif:
        possible_answers+=1
print(possible_answers)