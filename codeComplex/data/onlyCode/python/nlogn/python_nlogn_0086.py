import bisect

tmp = input().split()
n = int(tmp[0])
k = int(tmp[1])

scores = list()
times = list()
for i in range(n):
    tmp = input().split()
    scores.append(int(tmp[0]))
    times.append(int(tmp[1]))

sorted_scores = sorted(zip(scores, times), key=lambda y : (y[0], -y[1]), reverse=True)

ans = 1
i = k-2
while i>=0 and (sorted_scores[i] == sorted_scores[k-1]):
    ans = ans + 1 
    i = i - 1

i = k
while i < n and (sorted_scores[i] == sorted_scores[k-1]):
    ans = ans + 1 
    i = i + 1 

print(ans)