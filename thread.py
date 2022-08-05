# 命名是不应该使用模块名进行文件命名，否则python在查找模块时出现错误，
import threading
from time import sleep, ctime
from threading import Thread

def test1():
    """
    这是一个单独的任务
    """
    for i in range(10):
        print("任务1...%d" % i)
        sleep(0.1)

        
def test2():
    """
    这是另外一个单独的任务
    """
    for i in range(5):
        print("任务2...%d" % i)
        sleep(0.2)

def work1(num1, num2, m):
    print("任务3...----in work1--num1=%d,num2=%d,m=%d-" % (num1, num2, m))


def work2(num1, num2, num3, n):
    print("任务4...----in work1--num1=%d,num2=%d,num3=%d,n=%d-" % (num1, num2, num3, n))
        

t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)
t3 = Thread(target=work1, args=(11, 22), kwargs={"m": 100})
t4 = Thread(target=work2, args=(33, 44, 55), kwargs={"n": 200})
t1.start()
t2.start()
t3.start()
t4.start()