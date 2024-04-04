# increasing Traingle Pattern
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print(" ")    
    
    
#decreasing Traingle Pattern    
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')
#     print()    
  
  
#right sided traingle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print('',end='') 
#     for j in range(i+1):
#          print('*',end=' ')     
#     print()    

#decreasing right sided traingle
n=5 
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    for j in range(i,n):
        print('',end=' ')  
    print() 

#hill pattern
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end='')
#     for j in range(i):
#         print('*',end='') 
#     for j in range(i+1):
#         print('*',end='')           
#     print()    
    
#reverse hill
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(' ',end='') 
#     for j in range(i,n-1):
#         print('*',end='') 
#     for j in range(i,n):
#         print('*',end='')     
#     print()  
    
    
#diamond
n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='') 
    for j in range(i+1):
        print('*',end='')           
    print() 
    
for i in range(n):
    for j in range(i+1):
        print(' ',end='') 
    for j in range(i,n-1):
        print('*',end='') 
    for j in range(i,n):
        print('*',end='')     
    print()  
                  
            