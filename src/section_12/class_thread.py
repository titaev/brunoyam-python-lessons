from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self, start, end, timeout):
        Thread.__init__(self)
        self.start = start
        self.end = end
        self.timeout = timeout

    def run(self):
        while self.start < self.end:
            print("Thread: %s" % se;f.start)
            self.start += 1
            sleep(self.timeout)


thread1 = MyThread(3, 10, 1)
thread2 = MyThread(5, 20, 0.5)

thread1.start()
thread2.start()

for i in range(5):
    print("MAIN THREAD")
    sleep(0.5)

thread1.join()
thread2.join()

print("END")