import math

def solve(people, planes_each, per, sheets):
    sheets_per_person = math.ceil(planes_each / per)
    needed = sheets_per_person * people
    packs = math.ceil(needed / sheets)
    # print(packs)
    pass

def main(n):
    people = n
    planes_each = n + 1
    per = (n % 5) + 1
    sheets = (n % 7) + 1
    solve(people, planes_each, per, sheets)

if __name__ == "__main__":
    main(10)