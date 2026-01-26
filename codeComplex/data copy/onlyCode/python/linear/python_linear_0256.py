#!/usr/bin/python3
#Antipalindrome
s=input()
for i in range(len(s),0,-1):
    if s[:i]!=s[i-1::-1]:
        print(i)
        break
else:
    print(0)
