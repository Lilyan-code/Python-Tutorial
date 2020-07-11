import threading
import time
def thread_job_1():
  print("Thread1 start")
  for i in range(10):
    time.sleep(0.2)  #time.sleep(t)让程序睡眠t秒
  print("Thread1 end")
def main():
  added_thread1 = threading.Thread(target = thread_job_1, name = "Thread1")
  added_thread1.start() # 一定要启动刚刚添加的线程，不然线程不会自动进行工作.当代码运行后，至少会有一个main线程去执行
  added_thread1.join()
  print("All finish")
if __name__ == '__main__':
  main()