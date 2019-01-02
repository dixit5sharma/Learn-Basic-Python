def hanoi(size, start, middle, end):
    if size > 0 :
        hanoi( size-1 , start , end , middle )  #Move n-1 disks from A to B
        print( "Move disk" , size , "from" , start , "to" , end )   #Move the n disk from A to C
        hanoi( size-1 , middle , start , end )  #Move n-1 disks from B to C

n = int(input())
hanoi(n,"A","B","C")
