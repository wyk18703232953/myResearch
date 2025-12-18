import math

n=int(input())
k=1
while(n > 9*k*(10**(k-1))):
    n = n - 9*k*(10**(k-1))
    k = k + 1
remainder = n%k
if remainder == 0:
    remainder = k
if k==1:
    quoteint = math.ceil(n/k)
else:
    adder = "9"*(k-1)
    adder = int(adder)
    quoteint = math.ceil(n/k) + adder
print(str(quoteint)[remainder-1])




    
    
    
        
        
        
    

        
        
        
        
        
        
    


                        
                        
                    
        
 
        
  
    
    
                
                
                
            
            
     
                
    
            
            
        
    
  


    
   
        

  
            
  
    
    
    



            
            
            
    
    
            
   
    

    

            
            
    
    

    
    

        


    

    
    
    









            
            
        
        
        
        
    
        