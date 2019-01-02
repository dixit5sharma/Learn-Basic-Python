print("Enter a line to be splitted")
s=input()
print("Enter the regex")
reg=input()     #Input regex

a=s.split(reg)  #Space also works
print(a)
