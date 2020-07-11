import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)

if __name__ == '__main__':
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