import task_1, task_2, task_3
import time


with open("schedule.json", encoding='utf-8') as w:
    f = w.read() 

start_time = time.time()
for i in range(100):
    task_1.wrapper(eval(f))

print("--- %s seconds ---" % (time.time() - start_time), '    first-task')

start_time = time.time()
for i in range(100):
    task_2.convertor(f)

print("--- %s seconds ---" % (time.time() - start_time), '    second-task')

with open("schedule.json", encoding='utf-8') as w:
    f = w.readlines()[1:]
start_time = time.time()
for i in range(100):
    task_3.convertor(f)

print("--- %s seconds ---" % (time.time() - start_time), '    third-task')

