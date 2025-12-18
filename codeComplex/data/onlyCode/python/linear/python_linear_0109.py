first,last=input().split()
username=first[0]
first=first[1:]
while first!="" and first[0]<last[0]:
    username=username+first[0]
    first=first[1:]
print(username+last[0])