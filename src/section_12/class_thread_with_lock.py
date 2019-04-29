from threading import Thread, Lock
from time import sleep


count = 0
lock = Lock()


class MyThread(Thread):
    def __init__(self, end, timeout):
        Thread.__init__(self)
        self.end = end
        self.timeout = timeout

    def run(self):
        global count
        global lock
        while count < self.end:
            print("Thread: %s" % count)
            
            lock.aquire()
            try:
                count += 1
            finally:
                lock.release()
            
            sleep(self.timeout)


thread1 = MyThread(10, 1)
thread2 = MyThread(20, 0.5)

thread1.start()
thread2.start()

for i in range(5):
    print("MAIN THREAD")
    sleep(0.5)

thread1.join()
thread2.join()

print("END")