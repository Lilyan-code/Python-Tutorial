import multiprocessing as mp

def job(x) :
    return x * x

def multiProcess():
    pool = mp.Pool(processes = 4)
    res = pool.map(job, range(100))
    print(res)
    res = pool.apply_async(job, (2, ))
    print(res.get())
    multi_res = [pool.apply_async(job, (i, )) for i in range(100)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multiProcess()