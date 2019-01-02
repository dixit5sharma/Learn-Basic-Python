def Palindrome(a):
    if a==a[::-1]:
        print("This is a Palindrome")
    else:
        print("Not a palindrome")

print("Enter the string")
Palindrome(input())
