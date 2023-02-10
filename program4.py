# to print the next prime number

n=int(input())
import sys
for i in range(n+1,100):
    for j in range(2,i-1):
        if i%j==0:
           break
        else:

           print(i)
           sys.exit()

        
     

        
       
         
      



