import math
def solve():
    words = input().split()
    people = int(words[0])
    planes_each = int(words[1])
    per = int(words[2])
    sheets = int(words[3])
    sheets_per_person = math.ceil(planes_each/per)
    needed = sheets_per_person*people
    packs = math.ceil(needed/sheets)
    print(packs)

    

# for _ in range(int(input())):
solve()