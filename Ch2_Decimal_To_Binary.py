"""
This is a multiline comment.
This code is for conversion of decimal to Binary format.
"""

print("Enter number in decimal")
n=int(input())  #input fron user
i=n
converted=''

while i>0:
    rem=i%2
    converted=str(rem)+converted
    i=int(i/2)
print(converted)
    
