import time
import random
from random_word import RandomWords

random.seed(8)
int_list = []
float_list = []
str_list = []


w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.get_random_word())



def selection_sort(data):
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex
        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]


def average_time(list, r):
    t = 0
    for i in range(0, r):
        cur_time1 = time.time()
        list_sort=selection_sort(list)
        t=t+(time.time() - cur_time1)
        if i==r-1:
            t=t/r
    print(f"Average execution time: {t}")

average_time(int_list, 10)
average_time(float_list, 10)


