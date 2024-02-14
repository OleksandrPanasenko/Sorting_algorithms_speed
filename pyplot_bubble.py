from matplotlib import pyplot as plt
import random
import time

start=0
finish=2000
step=20

sizes = list(range(start, finish + 1, step))
y_array_average = []
y_array_good = []
y_array_bad = []
sizes=[10, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]

for size in sizes:
    array = list(range(size))
    # array.reverse()


    array_bubble = array.copy()
    count_comparisons = 0
    count_switches = 0
    begin = time.time()
    for i in range(0, len(array_bubble) - 1):
        for j in range(0, len(array_bubble) - 1):
            count_comparisons += 1
            if (array_bubble[j] > array_bubble[j + 1]):
                change = array_bubble[j]
                array_bubble[j] = array_bubble[j + 1]
                array_bubble[j + 1] = change
                count_switches += 1
    end = time.time()
    y_array_good.append(end - begin)

    array = list(range(size))
    array.reverse()

    array_bubble = array.copy()
    count_comparisons = 0
    count_switches = 0
    begin = time.time()
    for i in range(0, len(array_bubble) - 1):
        for j in range(0, len(array_bubble) - 1):
            count_comparisons += 1
            if (array_bubble[j] > array_bubble[j + 1]):
                change = array_bubble[j]
                array_bubble[j] = array_bubble[j + 1]
                array_bubble[j + 1] = change
                count_switches += 1
    end = time.time()
    y_array_bad.append(end - begin)

    array = list(range(size))
    array.reverse()
    for i in range(1):
        random.shuffle(array)

    array_bubble = array.copy()
    count_comparisons = 0
    count_switches = 0
    begin = time.time()
    for i in range(0, len(array_bubble) - 1):
        for j in range(0, len(array_bubble) - 1):
            count_comparisons += 1
            if (array_bubble[j] > array_bubble[j + 1]):
                change = array_bubble[j]
                array_bubble[j] = array_bubble[j + 1]
                array_bubble[j + 1] = change
                count_switches += 1
    end = time.time()
    y_array_average.append(end - begin)

plt.title("Bubble sort algorithm")
plt.xlabel("Size of array")
plt.ylabel("Time (in seconds)")
plt.plot(sizes, y_array_average, label="random array", color="blue")
plt.plot(sizes, y_array_good, label="ordered array", color="green")
plt.plot(sizes, y_array_bad, label="reversed array", color="red")
plt.legend(["random values", "ordered array/best time possible", "reversed ordered/worst time possible"])
plt.show()