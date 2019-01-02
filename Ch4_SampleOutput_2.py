Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array.py =============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Dictionary_Array.py", line 18, in <module>
    print(contacts["name2"])
TypeError: list indices must be integers or slices, not str
>>> 
============= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array.py =============
[{'name1': 9999999999, 'name2': 9999999999, 'name3': 9999999999}, {'name4': 9999999999, 'name2': 9999999999}, {'name3': 9999999999, 'name5': 9999999999, 'name6': 9999999999}]
>>> 
============= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array.py =============
{'name1': 9999999999, 'name2': 9999999999, 'name3': 9999999999}
{'name4': 9999999999, 'name2': 9999999999}
{'name3': 9999999999, 'name5': 9999999999, 'name6': 9999999999}
>>> 
============= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array.py =============
name1
name2
name3
name4
name2
name3
name5
name6
>>> 
============= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array.py =============
9999999999
9999999999
9999999999
9999999999
9999999999
9999999999
9999999999
9999999999
>>> 
============= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array.py =============
name1 = 9999999999
name2 = 9999999999
name3 = 9999999999
name4 = 9999999999
name2 = 9999999999
name3 = 9999999999
name5 = 9999999999
name6 = 9999999999
>>> 
============ RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_2.py ============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Dictionary_Array_2.py", line 18, in <module>
    print(contacts[school])
NameError: name 'school' is not defined
>>> 
============ RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_2.py ============
{'name1': 9999999999, 'name2': 9999999999, 'name3': 9999999999}
>>> 
============ RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_2.py ============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Dictionary_Array_2.py", line 18, in <module>
    for k,v in contacts:
ValueError: too many values to unpack (expected 2)
>>> 
============ RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_2.py ============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Dictionary_Array_2.py", line 18, in <module>
    for k,v in contacts:
ValueError: too many values to unpack (expected 2)
>>> 
============ RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_2.py ============
school = {'name1': 9999999999, 'name2': 9999999999, 'name3': 9999999999}
college = {'name4': 9999999999, 'name2': 9999999999}
work = {'name3': 9999999999, 'name5': 9999999999, 'name6': 9999999999}
>>> 
============ RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_2.py ============
school = {'name1': 9999999999, 'name2': 9999999999, 'name3': 9999999999}
name1 = 9999999999
name2 = 9999999999
name3 = 9999999999
college = {'name4': 9999999999, 'name2': 9999999999}
name4 = 9999999999
name2 = 9999999999
work = {'name3': 9999999999, 'name5': 9999999999, 'name6': 9999999999}
name3 = 9999999999
name5 = 9999999999
name6 = 9999999999
>>> 
====== RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Comprehension.py ======
['name1', 'name2', 'name2']
>>> 
====== RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Comprehension.py ======
[{'name': 'name1', 'year': 1, 'cpi': 8.5, 'dept': 'ECE'}, {'name': 'name2', 'year': 2, 'cpi': 8.2, 'dept': 'MNC'}, {'name': 'name2', 'year': 3, 'cpi': 8.1, 'dept': 'CSE'}]
['name1', 'name2', 'name2']
>>> 
====== RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Comprehension.py ======
[{'name': 'name1', 'year': 1, 'cpi': 8.5, 'dept': 'ECE'}, {'name': 'name2', 'year': 2, 'cpi': 8.2, 'dept': 'MNC'}, {'name': 'name2', 'year': 3, 'cpi': 8.1, 'dept': 'CSE'}]
['name1', 'name2', 'name2']
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Dictionary_Array_Comprehension.py", line 27, in <module>
    pritn(i["name"])
NameError: name 'pritn' is not defined
>>> 
====== RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Comprehension.py ======
[{'name': 'name1', 'year': 1, 'cpi': 8.5, 'dept': 'ECE'}, {'name': 'name2', 'year': 2, 'cpi': 8.2, 'dept': 'MNC'}, {'name': 'name2', 'year': 3, 'cpi': 8.1, 'dept': 'CSE'}]
['name1', 'name2', 'name2']
name1
name2
name2
>>> 
======= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Application.py =======
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Dictionary_Array_Application.py", line 15, in <module>
    students[rn].append(cs)
KeyError: 'M'
>>> 
>>> 
======= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Application.py =======
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Dictionary_Array_Application.py", line 15, in <module>
    students[rn].append(cs)
KeyError: 'M'
>>> 
======= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Application.py =======
{'140101001': ['CS101', 'EE101', 'CS201', 'MA321'], '140102001': ['MA101', 'EE101', 'EE201', 'EE301'], '140103001': ['CS101', 'ME101', 'EE301', 'ME301'], '140123001': ['MA101', 'CS101', 'MA201', 'MA321']}
>>> 
======= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Application.py =======
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Dictionary_Array_Application.py", line 17, in <module>
    for k,v in students:
ValueError: too many values to unpack (expected 2)
>>> 
======= RESTART: C:/Python371/MyP/Ch4_Dictionary_Array_Application.py =======
140101001 = ['CS101', 'EE101', 'CS201', 'MA321']
140102001 = ['MA101', 'EE101', 'EE201', 'EE301']
140103001 = ['CS101', 'ME101', 'EE301', 'ME301']
140123001 = ['MA101', 'CS101', 'MA201', 'MA321']
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
A is a integer
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
C and D both are String
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
C and D both are String
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
C and D both are String
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
C and D both are String
fwefw
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
C and D both are String
Integer
List
String
String
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
Traceback (most recent call last):
  File "C:/Python371/MyP/Ch4_Type_Function.py", line 5, in <module>
    e = {name:"name1",rollno:"45"}
NameError: name 'name' is not defined
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
C and D both are String
Integer
List
String
String
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'dict'>
C and D both are String
Integer
List
String
String
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'dict'>
C and D both are String
Integer
List
String
String
Dictionary
>>> 
=============== RESTART: C:/Python371/MyP/Ch4_Type_Function.py ===============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
<class 'dict'>
C and D both are String
Integer
List
String
String
Dictionary
>>> 
============ RESTART: C:/Python371/MyP/Ch4_Isinstance_Function.py ============
<class 'int'>
<class 'list'>
<class 'str'>
<class 'str'>
<class 'dict'>
C and D both are String
Integer
List
String
String
Dictionary
>>> 
============ RESTART: C:/Python371/MyP/Ch4_Isinstance_Function.py ============
Integer
List
String
String
Dictionary
>>> 
