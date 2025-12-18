def process(S):
    n = len(S)
    h_count = 0
    answer = float('inf')
    for c in S:
        if c=='H':
            h_count+=1
    current = 0
    for i in range(h_count):
        if S[i]=='H':
            current+=1
    answer = min(answer, h_count-current)
    for i in range(h_count, n+h_count):
        if i > n-1:
            i1 = i-n
        else:
            i1 = i 
        i2 = i-h_count
        if S[i1]=='H':
            current+=1
        if S[i2]=='H':
            current-=1
        answer = min(answer, h_count-current)
    return answer

n = int(input())
S = input()
print(process(S))