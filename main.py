
# Online Python - IDE, Editor, Compiler, Interpreter
def is_pratt(num):
    num=int(num)
    while (num%2==0):
        num=int(num/2)
    while (num%3==0):
        num=int(num/3)
    return num==1

import random
import time
#filling array with values
a = " "
while (a != "0" and a != "1"):
    a = input("0-manual input, 1 - generate ")
sizes=[10, 100, 1000, 5000, 10000, 20000, 50000]
array = []
for size in sizes:
    array=list(range(size))
    array.reverse()
    '''
    if (a == "0"):
        array = input("enter elements of the array ").split()
        for i in range(len(array)):
            array[i] = float(array[i])
    else:
        #fill with numbers in random order
        array = list(range(int(input("Length of the array: "))))
        '''
    for i in range (len(array)):
        random.shuffle(array)
    print("Generated array: ")
    print(array)

    array_bubble=array.copy()
    count_comparisons = 0
    count_switches = 0
    begin=time.time()
    for i in range(0, len(array_bubble) - 1):
        for j in range(0, len(array_bubble) - 1):
            count_comparisons+=1
            if (array_bubble[j] > array_bubble[j + 1]):
                change = array_bubble[j]
                array_bubble[j] = array_bubble[j + 1]
                array_bubble[j + 1] = change
                count_switches+=1
    end=time.time()

    print("Plain bubble:")
    #print(array_bubble)
    print(str(size)+" Elements;\nNumber of checks:"+str(count_comparisons)+";\nNumber of changes: "+str(count_switches)+"\nTotal time: "+str(end-begin))
    #bubble advanced
    count_comparisons=0
    count_switches=0
    array_bubble=array.copy()
    begin=time.time()
    for i in range(0, len(array_bubble) - 1):
        for j in range(0, len(array_bubble) - 1-i):
            count_comparisons+=1
            if (array_bubble[j] > array_bubble[j + 1]):
                change = array_bubble[j]
                array_bubble[j] = array_bubble[j + 1]
                array_bubble[j + 1] = change
                count_switches+=1
    end=time.time()
    print("Bubble modified:")
    #print(array_bubble)
    print(str(size)+" Elements;\nNumber of checks:"+str(count_comparisons)+";\nNumber of changes: "+str(count_switches)+"\nTotal time: "+str(end-begin))
    #shell sort
    '''count_comparisons=0
    count_switches=0
    array_shell=array.copy()
    i=len(array_shell)
    begin=time.time()
    while(i>1):
        i=int((i-1)/2+1)
        for j in range(0, len(array_shell)-i):
            count_comparisons+=1
            if(array_shell[j+i]>array_shell[j]):
                change=array_shell[i+j]
                array_shell[i+j]=array_shell[j]
                array_shell[j]=change
                count_switches+=1
    end=time.time()
    print("Sorted array (shell algorithm):")
    #print(array_shell)
    print("Number of checks:"+str(count_comparisons)+";\nNumber of changes: "+str(count_switches)+"\nTotal time: "+str(end-begin))
    '''
    #shell sort
    count_comparisons=0
    count_switches=0
    array_shell_pratt=array.copy()
    i=len(array_shell_pratt)
    begin=time.time()
    for i in range (len(array_shell_pratt)-1, 0,-1):
        if (is_pratt(i)):
            for j in range(0, len(array_shell_pratt)-i):
                count_comparisons+=1
                if(array_shell_pratt[j+i]<array_shell_pratt[j]):
                    change=array_shell_pratt[i+j]
                    array_shell_pratt[i+j]=array_shell_pratt[j]
                    array_shell_pratt[j]=change
                    count_switches+=1
    end=time.time()
    print("Shell pratt algorithm:")
    #print(array_shell_pratt)
    print(str(size)+" Elements;\nNumber of checks:"+str(count_comparisons)+";\nNumber of changes: "+str(count_switches)+"\nTotal time: "+str(end-begin))
