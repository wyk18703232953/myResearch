
s=input()


while(1):
        if(len(s)==1):
                print(0)
                break
            
        elif(s==s[::-1]):
            
            s=s[1:]
        
        
        
        else:
            print(len(s))
            break