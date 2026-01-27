import math

k,n,s,p = input().split()
k = int(k)      #no of person
n = int(n)      #no of planes each will make
s = int(s)      #no of planes that can be made in one sheet
p = int(p)      #no of sheet in one pack

sheet_for_each_person = math.ceil(n/s)
# print(sheet_for_each_person)
total_sheets_required = k*sheet_for_each_person
# print(total_sheets_required)
no_of_packs = math.ceil( total_sheets_required/p )
print(no_of_packs)