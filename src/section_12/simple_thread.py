from threading import Thread
from time import sleep


def func1(start, end):
    while start < end:
        print("Func1: %s" % start)
        start += 1
        sleep(1)


def func2(start, end):
    while start < end:
        print("Func2: %s" % start)
        start += 1
        sleep(0.5)


thread1 = Thread(target=func1, args=(3, 10))
thread2 = Thread(target=func2, args=(5, 20))
thread1.start()
thread2.start()

for i in range(5):
    print("MAIN THREAD")
    sleep(0.5)

thread1.join()
thread2.join()

print("END")