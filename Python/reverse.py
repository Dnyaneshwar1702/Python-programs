"""Solution 1"""

# num=1234
# num=str(num)
# print(num[::-1])


"""solution 2"""
num=int(input("Enter a number  "))
reversed=0
while num>0:
    rem=num%10
    reversed=reversed*10+rem
    num//=10
print(reversed)
if  reversed!=num:
    print("Reversed is true")
    
