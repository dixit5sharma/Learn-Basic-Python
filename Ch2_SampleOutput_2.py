Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Square_Of_List.py ==============
Enter number of elements
5
Enter number 0
1
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Square_Of_List.py", line 10, in <module>
    b.append(temp**2)
NameError: name 'b' is not defined
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Square_Of_List.py ==============
Enter number of elements
5
Enter number 0
1
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Square_Of_List.py", line 11, in <module>
    b.append(temp)
NameError: name 'b' is not defined
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Square_Of_List.py ==============
Enter number of elements
5
Enter number 0
1
Enter number 1
4
Enter number 2
7
Enter number 3
3
Enter number 4
9
Input [1, 4, 7, 3, 9]
Output [1, 16, 49, 9, 81]
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Square_Of_List.py ==============
Enter number of elements
5
Enter number 1
1
Enter number 2
3
Enter number 3
5
Enter number 4
7
Input [1, 3, 5, 7]
Output [1, 9, 25, 49]
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Square_Of_List.py ==============
Enter number of elements
5
Enter number 0
1
Enter number 1
4
Enter number 2
6
Enter number 3
3
Enter number 4
6
Input [1, 4, 6, 3, 6]
Output [1, 16, 36, 9, 36]
>>> 
============= RESTART: C:/Python371/MyP/Ch2_String_Append_Try.py =============
Enter number of elements
5
Enter element 0
1
Enter element 1
"Dixit"
Enter element 2
Sharma
Enter element 3
tyrt
Enter element 4
fg
Input ['1', '"Dixit"', 'Sharma', 'tyrt', 'fg']
>>> rt
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    rt
NameError: name 'rt' is not defined
>>> run
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    run
NameError: name 'run' is not defined
>>> 
============= RESTART: C:/Python371/MyP/Ch2_String_Append_Try.py =============
Enter number of elements
5
Enter element 0
34
Enter element 1
657
Enter element 2
thrg
Enter element 3
fgbf
Enter element 4
ui
Input ['34', '657', 'thrg', 'Sharma', 'ui']
>>> 
============= RESTART: C:/Python371/MyP/Ch2_String_Append_Try.py =============
Enter number of elements
4
Enter element 0
sdfge
Enter element 1
ujyu
Enter element 2
fdg
Enter element 3
rgt
Input ['sdfge', 'ujyu', 'Sharma', 'rgt']
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Split_String.py ===============
Enter a line to be splitted
234+-+4534+-+3453+-+3545+-+354+-+53
Enter the regex
+-+
['234', '4534', '3453', '3545', '354', '53']
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Split_String.py ===============
Enter a line to be splitted
This is a try
Enter the regex
 
['This', 'is', 'a', 'try']
>>> 
>>> 
>>> 
================ RESTART: C:/Python371/MyP/Ch2_Join_String.py ================
Enter the joining element
 
Dixit Sharma is Learning
>>> 
================ RESTART: C:/Python371/MyP/Ch2_Join_String.py ================
Enter the joining element
/
Dixit/Sharma/is/Learning
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Length_Function.py ==============
5
4
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Length_Function.py", line 8, in <module>
    print(len(c))
TypeError: object of type 'int' has no len()
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Length_Function.py ==============
5
4
4
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Length_Function.py ==============
8
5
4
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Length_Function.py ==============
6
5
4
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Min_Function.py ===============
0
czzz
D
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Min_Function.py ===============
0
czzz
Z
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Min_Function.py ===============
0
czzz
i
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Min_Function.py ===============
0
Pabc
i
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Min_Function.py ===============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Min_Function.py", line 5, in <module>
    print(min(a))   #Lowest number in the series is the min.
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Min_Function.py ===============
0
czzz
Z
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Max_Function.py ===============
6
pabc
x
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Sum_Function.py ===============
993
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Sum_Function.py ===============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Sum_Function.py", line 3, in <module>
    print(sum(num))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Sum_Function.py ===============
993
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Sum_Function.py ===============
994
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Sort_Function.py ===============
Input A [0, 1, 3, 6]
Sorted None
Input B ['five', 'four', 'one', 'three', 'two']
Sorted None
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Sort_Function.py ===============
Input A [3, 6, 1, 0]
Sorted [0, 1, 3, 6]
Input B ['one', 'two', 'three', 'four', 'five']
Sorted ['five', 'four', 'one', 'three', 'two']
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Sort_Function.py ===============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Sort_Function.py", line 5, in <module>
    mix.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Find_Function_1.py ==============
Enter a number to find
3
Present
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Find_Function_1.py ==============
Enter a number to find

67
Not Present
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Find_Function_1.py ==============
Input String [1, 2, 3, 4, 5, 6, 7, 8, 9]
Enter a number to find
9
Present
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Find_Function_2.py ==============
Input String ['Dixit', 'Sharma', 'is', 'Learning']
Enter element to find
is
Present
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Find_Function_2.py ==============
Input String ['Dixit', 'Sharma', 'is', 'Learning']
Enter element to find
not
Not Present
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Find_Function_3.py ==============
Input String Dixit Sharma is Learning
Enter character to find
is
Present
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Find_Function_3.py ==============
Input String Dixit Sharma is Learning
Enter character to find
e
Present
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Find_Function_3.py ==============
Input String Dixit Sharma is Learning
Enter character to find
z
Not Present
>>> 
============ RESTART: C:/Python371/MyP/Ch2_Find_Function_4_Try.py ============
Input String - ['Dixit', 'Sharma', 'is', 'Learning', 21, 324, 423]
Enter element to find
2
Not Present
>>> 
============ RESTART: C:/Python371/MyP/Ch2_Find_Function_4_Try.py ============
Input String - ['Dixit', 'Sharma', 'is', 'Learning', 21, 324, 423]
Enter element to find
21
Not Present
>>> 
============ RESTART: C:/Python371/MyP/Ch2_Find_Function_4_Try.py ============
Input String - ['Dixit', 'Sharma', 'is', 'Learning', 21, 324, 423]
Enter element to find
324
Not Present
>>> 
============ RESTART: C:/Python371/MyP/Ch2_Find_Function_4_Try.py ============
Input String - ['Dixit', 'Sharma', 'is', 'Learning', 21, 324, 423]
Enter element to find
is
Present
>>> 
============ RESTART: C:/Python371/MyP/Ch2_Find_Function_4_Try.py ============
Input String - ['Dixit', 'Sharma', 'is', 'Learning', 21, 324, 423]
Enter element to find
"21"
Not Present
>>> 
============ RESTART: C:/Python371/MyP/Ch2_Find_Function_4_Try.py ============
Input String - ['Dixit', 'Sharma', 'is', 'Learning', 21, 324, 423]
Enter element to find
'21'
Not Present
>>> 
============ RESTART: C:/Python371/MyP/Ch2_Find_Function_4_Try.py ============
Input String - ['Dixit', 'Sharma', 'is', 'Learning', 21, 324, 423]
Enter element to find
21
Present
>>> 
============ RESTART: C:/Python371/MyP/Ch2_Find_Function_4_Try.py ============
Input String - ['Dixit', 'Sharma', 'is', 'Learning', 21, 324, 423]
Enter element to find
is
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Find_Function_4_Try.py", line 4, in <module>
    f=int(input())
ValueError: invalid literal for int() with base 10: 'is'
>>> 
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Mean_Function.py ===============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Mean = 6.125
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Median_Function.py", line 8, in <module>
    median=(a[first]+a[first+1])/2
TypeError: list indices must be integers or slices, not float
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Median_Function.py", line 9, in <module>
    median=(int(a[first]+a[second]))/2
TypeError: list indices must be integers or slices, not float
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Median_Function.py", line 9, in <module>
    median=(int(a[first]+a[second]))/2
TypeError: list indices must be integers or slices, not float
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Median_Function.py", line 9, in <module>
    median=(float(a[first]+a[second]))/2
TypeError: list indices must be integers or slices, not float
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Median_Function.py", line 10, in <module>
    temp=a[first]+a[second]
TypeError: list indices must be integers or slices, not float
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
4.0
5.0
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Median_Function.py", line 12, in <module>
    temp=a[first]+a[second]
TypeError: list indices must be integers or slices, not float
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Median = 7.5
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Sorted String - [2, 3, 3, 5, 7, 8, 9, 12]
Median = 7.5
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9]
Sorted String - [2, 3, 3, 5, 7, 8, 9, 12]
Median = 6.0
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9, 10]
Sorted String - [2, 3, 3, 5, 7, 8, 9, 10, 12]
Median = 8
>>> 
============== RESTART: C:/Python371/MyP/Ch2_Median_Function.py ==============
Input String - [8, 2, 3, 12, 5, 3, 7, 9, 10]
Sorted String - [2, 3, 3, 5, 7, 8, 9, 10, 12]
Median = 7
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Prime_Upto100.py ===============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Prime_Upto100.py", line 5, in <module>
    print(a[101])
IndexError: list index out of range
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Prime_Upto100.py ===============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Prime_Upto100.py", line 5, in <module>
    print(a[100])
IndexError: list index out of range
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Prime_Upto100.py ===============
1
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Prime_Upto100.py ===============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Prime_Upto100.py", line 3, in <module>
    a[i]=1
IndexError: list assignment index out of range
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Prime_Upto100.py ===============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch2_Prime_Upto100.py", line 2, in <module>
    a[i]=1
NameError: name 'a' is not defined
>>> 
=============== RESTART: C:/Python371/MyP/Ch2_Prime_Upto100.py ===============
1
>>> 
