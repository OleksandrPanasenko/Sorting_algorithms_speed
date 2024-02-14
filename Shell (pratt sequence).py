def is_pratt(num):
    num=int(num)
    while (num%2==0):
        num=int(num/2)
    while (num%3==0):
        num=int(num/3)
    return num==1

from matplotlib import pyplot as plt
import random
import time
import math
start=0
step=100
finish=50000
array_pratt=[]
for i in range(int(math.log(finish,3)), -1, -1) :
    for j in range(int(math.log(finish/(3.0**i), 2)), -1, -1):
        array_pratt.append((3**i)*2**j)
print(array_pratt)


#sizes = list(range(start, finish + 1, step))
y_array_average = []
y_array_good = []
y_array_bad = []
sizes=list(range(start, finish+1, step))

for size in sizes:
    array = list(range(size))
    # array.reverse()

    #sorted already
    array_shell_pratt = array.copy()
    count_comparisons = 0
    count_switches = 0
    begin = time.time()
    for i in array_pratt:
        if (is_pratt(i)):
            for j in range(0, len(array_shell_pratt)-i):
                count_comparisons+=1
                if(array_shell_pratt[j+i]<array_shell_pratt[j]):
                    change=array_shell_pratt[i+j]
                    array_shell_pratt[i+j]=array_shell_pratt[j]
                    array_shell_pratt[j]=change
                    count_switches+=1
    end = time.time()
    y_array_good.append(end - begin)
    print("Progress")

#sorted in reversed order
    begin=time.time()
    array = list(range(size))
    array.reverse()
    end=time.time()
    print(end-begin)

    array_shell_pratt = array.copy()
    count_comparisons = 0
    count_switches = 0
    begin = time.time()
    for i in array_pratt:
        if (is_pratt(i)):
            for j in range(0, len(array_shell_pratt)-i):
                count_comparisons+=1
                if(array_shell_pratt[j+i]<array_shell_pratt[j]):
                    change=array_shell_pratt[i+j]
                    array_shell_pratt[i+j]=array_shell_pratt[j]
                    array_shell_pratt[j]=change
                    count_switches+=1
    end = time.time()
    y_array_bad.append(end - begin)
#randomize
    begin=time.time()
    array = list(range(size))
    array.reverse()
    for i in range(1):
        random.shuffle(array)
    end=time.time()
    print(end-begin)
#random order
    array_shell_pratt = array.copy()
    count_comparisons = 0
    count_switches = 0
    begin = time.time()
    for i in array_pratt:
        if (is_pratt(i)):
            for j in range(0, len(array_shell_pratt)-i):
                count_comparisons+=1
                if(array_shell_pratt[j+i]<array_shell_pratt[j]):
                    change=array_shell_pratt[i+j]
                    array_shell_pratt[i+j]=array_shell_pratt[j]
                    array_shell_pratt[j]=change
                    count_switches+=1
    end = time.time()
    y_array_average.append(end - begin)
print("done")

plt.title("Shell method (Pratt sequence)")
plt.xlabel("Size of array")
plt.ylabel("Time (in seconds)")
plt.plot(sizes, y_array_average, label="random array", color="blue")
plt.plot(sizes, y_array_good, label="ordered array", color="green")
plt.plot(sizes, y_array_bad, label="reversed array", color="red")
plt.legend(["random values", "ordered array/best time possible", "reversed ordered/worst time possible"])
plt.show()