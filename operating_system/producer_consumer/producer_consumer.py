import time
import random
import threading

queue = []
MAX_NUM = 2
condition = threading.Condition()


class Produce(threading.Thread):
    def run(self):
        tid = threading.get_ident()
        num = 1
        global queue

        while True:
            condition.acquire()

            while len(queue) == MAX_NUM:
                print("Queue is full", tid, "is waiting....")
                condition.wait()
                print(tid, "wake up")

            if len(queue) == 0:
                condition.notify()
            queue.append(num)
            print("Produced", num)
            condition.release()
            num += 1
            time.sleep(random.random())


class Consume(threading.Thread):
    def run(self):
        global queue
        tid = threading.get_ident()

        while True:
            condition.acquire()

            while len(queue) == 0:
                print("queue is empty", tid,  "is waiting...")
                condition.wait()
                print(tid, "wake up")

            if len(queue) == MAX_NUM:
                condition.notify()
            print("consumed", queue.pop(0))
            condition.release()
            time.sleep(random.random())


Produce().start()
Consume().start()
