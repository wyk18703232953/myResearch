
string = str(input())
length = len(string)

counter = 0
li = []
match_li = []

for i in range(length):
    letter = string[i]
    letters = letter
    if letter in li:
        match_li.append(letter)
    li.append(letter)
    for j in range(i+1, length):
        letters += string[j]
        if letters in li:
            match_li.append(letters)
        li.append(letters)

longest = 0
for k in match_li:
    if len(k) > longest:
        longest = len(k)

print(longest)
    
