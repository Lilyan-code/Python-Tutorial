import threading
import time
from queue import Queue
def thread_work(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)

def multithreading_work():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(3):
        t = threading.Thread(target= thread_work, args=(data[i], q)) # 创建线程中方法使用args添加参数
        t.start()
        threads.append(t)
    for thread in threads: # 控制每个线程依次执行
        thread.join()
    results = []
    for i in range(3):
        results.append(q.get())
    print(results)
if __name__ == '__main__':
    multithreading_work()