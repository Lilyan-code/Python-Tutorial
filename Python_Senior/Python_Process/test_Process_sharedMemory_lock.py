import multiprocessing as mp
import time

def job(v, num, lock):
    lock.acquire()
    for i in range(10):
        time.sleep(0.2)
        v.value += num
        print(v.value)
    lock.release()

def multiProcess():
    lock = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job, args=(v, 10, lock))
    p2 = mp.Process(target=job, args=(v, 100, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multiProcess()