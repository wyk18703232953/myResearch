k, n, s, p = map(int, input().split())

paper_person = (n + s -1)//s

total_needed = paper_person * k

ans = (total_needed+p-1)//p

print(ans)


