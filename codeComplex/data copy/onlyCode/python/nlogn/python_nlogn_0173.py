length = int(input())
start = []
end = []
for i in range(length):
    a, b = map(int, input().split(" "))
    e, s = a - b, a + b
    end.append([e, i])
    start.append([s, i])
end.sort(key = lambda x:x[0])
start.sort(key = lambda x:x[0])
cant_visit = set()
answer = 0
end_index = 0
for s, i in start:
    if i not in cant_visit:
        answer += 1
        while end_index < length and end[end_index][0] < s:
            cant_visit |= {end[end_index][1]}
            end_index += 1            
print(answer)