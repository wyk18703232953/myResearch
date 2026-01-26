rank = 1
n = int(input())
score = sum(map(int,input().split()))
for i in range(n-1):
    student = sum(map(int,input().split()))
    if(student > score):
        rank += 1
print(rank)