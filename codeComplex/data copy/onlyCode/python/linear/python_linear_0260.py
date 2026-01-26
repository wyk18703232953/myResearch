s = input()
def is_pal(s):
      if s == s[::-1]:
            return True
      else:
            return False
if not is_pal(s):
      print(len(s))
else:
      not_eq = False
      for i in range(len(s)-1):
            if s[i] != s[i+1]:
                  print(len(s)-1)
                  not_eq = True
                  break
      if not not_eq:
            print(0)