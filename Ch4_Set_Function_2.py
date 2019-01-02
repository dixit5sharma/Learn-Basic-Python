rolls1 = {2,4,7,6,5,8}
rolls2 = {1,6,8,3,9,7}

rolls_uni = rolls1 | rolls2 # Elements in 1 and 2 combined
rolls_int = rolls1 & rolls2 # Elements common in 1 and 2
rolls_xor = rolls1 ^ rolls2 # Elements not common in both
rolls_1d2 = rolls1 - rolls2 # Elements in 1 not in 2
rolls_2d1 = rolls2 - rolls1 # Elements in 2 not in 1
print(rolls_uni) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(rolls_int) # {8, 6, 7}
print(rolls_xor) # {1, 2, 3, 4, 5, 9}
print(rolls_1d2) # {2, 4, 5}
print(rolls_2d1) # {1, 3, 9}
