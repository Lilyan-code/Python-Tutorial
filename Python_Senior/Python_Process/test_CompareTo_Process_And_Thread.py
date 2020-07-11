import multiprocessing as mp
import threading as tp
import time
def job(q):
    res = 0
    for i in range(1000000):
        res += i + i ** 2 + i ** 3
    q.put(res)

def MultiProcessJob():
    q = mp.Queue()
    p1 = mp.Process(target= job, args = (q, )) #注意这里的args即使只有一个参数，也必须加上逗号，表示这个参数是一个可迭代的对象
    p2 = mp.Process(target= job, args = (q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('Process1 compute result1: %d' % res1)
    print('Process2 compute result2: %d' % res2)

def MultiThreadJob():
    q = mp.Queue()
    t1 = tp.Thread(target= job, args = (q, )) #注意这里的args即使只有一个参数，也必须加上逗号，表示这个参数是一个可迭代的对象
    t2 = tp.Thread(target= job, args = (q, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res3 = q.get()
    res4 = q.get()
    print('Thread1 compute result3: %d' % res3)
    print('Thread2 compute result4: %d' % res4)

def NormalJob():
    res = 0
    for i in range(2):
        for j in range(1000000):
            res += i + i ** 2 + i ** 3
    print('Normal compute result5: %d' % res)

if __name__ == '__main__':
    st = time.time()
    NormalJob()
    ft = time.time()
    print('Normal Time is:', ft - st)
    st1 = time.time()
    MultiThreadJob()
    ft1 = time.time()
    print('MultiThread Time is', ft1 - st1)
    st2 = time.time()
    MultiProcessJob()
    ft2 = time.time()
    print('MultiProcess Time is', ft2 - st2)