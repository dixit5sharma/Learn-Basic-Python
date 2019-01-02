Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:/Python371/MyP/Ch4_Tuples.py ==================
Enter the number of points : 3
Enter 3 decimals separated by space for each point
Coordinates for point 1 : 2.1 4.5 6.7
Coordinates for point 2 : 8.5 6.8 9.0
Coordinates for point 3 : 2 4 7
[(2.1, 4.5, 6.7), (8.5, 6.8, 9.0), (2.0, 4.0, 7.0)]
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Zip_Function.py ===============
Enter list of number to be entered in a list separated by space: 1 2 3 4 5
Enter same number of another list of number to be entered in a list separated by space: 9 8 7 6 5
Zip of both list - [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]
>>> 
>>> 
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Zip_Function_2.py ==============
Enter list of number to be entered in a list separated by space: 1 2 3 4 5 6 7 8 9
Enter different number of another list of number to be entered in a list separated by space: 12 34 5 6 8
Enter different number of another list of number to be entered in a list separated by space: 23 67 09 7 4 3 
Zip of both list - [(1, 12, 23), (2, 34, 67), (3, 5, 9), (4, 6, 7), (5, 8, 4)]
>>> 
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Enter numbers space separated - 1 2 3
[1, 2, 3]
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Enter numbers space separated - 1 2 3
Enter numbers space separated - 3 4 5
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Add_2_Matrices.py", line 1, in <module>
    a=list(map(int,list(map(int,input("Enter numbers space separated - ").split())),list(map(int,input("Enter numbers space separated - ").split()))))
TypeError: int() can't convert non-string with explicit base
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Enter numbers space separated - 1 2 3
Enter numbers space separated - 3 4 5
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Add_2_Matrices.py", line 1, in <module>
    a=list(map(list,list(map(int,input("Enter numbers space separated - ").split())),list(map(int,input("Enter numbers space separated - ").split()))))
TypeError: list expected at most 1 arguments, got 2
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Enter numbers space separated - 1 2 3 
Enter numbers space separated - 3 4 5
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Add_2_Matrices.py", line 1, in <module>
    a=list(map(list(map(int,input("Enter numbers space separated - ").split())),list(map(int,input("Enter numbers space separated - ").split()))))
TypeError: 'list' object is not callable
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
3
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Add_2_Matrices.py", line 12, in <module>
    ans[i].append(a[i][j]+b[i][j])
IndexError: list index out of range
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Add_2_Matrices.py", line 12, in <module>
    ans[i].append(int(a[i][j])+int(b[i][j]))
IndexError: list index out of range
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Add_2_Matrices.py", line 17, in <module>
    if(flag==0):
NameError: name 'flag' is not defined
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
[[3, -10, 3, 15], [19, 8, 11, -3], [-1, 17, -4, -2]]
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Element a = [[3, -5, -7, 9], [13, 0, -2, 1], [-9, 8, 3, -1]]
Element b = [[0, -5, 10, 6], [6, 8, 13, -4], [8, 9, -7, -1]]
Addition = [[3, -10, 3, 15], [19, 8, 11, -3], [-1, 17, -4, -2]]
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Element a = [[3, -5, -7, 9], [13, 0, -2, 1], [-9, 8, 3, -1]]
Element b = [[0, -5, 10], [6, 8, 13, -4], [8, 9, -7, -1]]
Addition of Matrices not possible
>>> 
============== RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices.py ==============
Element a = [[3, -5, -7, 9], [13, 0, -2, 1], [-9, 8, 3, -1]]
Element b = [[0, -5, 10, 8], [6, 8, 13, -4], [8, 9, -7, -1]]
Addition = [[3, -10, 3, 17], [19, 8, 11, -3], [-1, 17, -4, -2]]
>>> 
============= RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices_2.py =============
Element a = [[3, -5, -7, 9], [13, 0, -2, 1], [-9, 8, 3, -1]]
Element b = [[0, -5, 10, 8], [6, 8, 13, -4], [8, 9, -7, -1]]
Addition = [[], [3, -10, 3, 17], [], [19, 8, 11, -3], [], [-1, 17, -4, -2]]
>>> 
============= RESTART: C:/Python371/MyP/Ch4_Add_2_Matrices_2.py =============
Element a = [[3, -5, -7, 9], [13, 0, -2, 1], [-9, 8, 3, -1]]
Element b = [[0, -5, 10, 8], [6, 8, 13, -4], [8, 9, -7, -1]]
Addition = [[3, -10, 3, 17], [19, 8, 11, -3], [-1, 17, -4, -2]]
>>> 
