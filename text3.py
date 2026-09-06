import time
import threading


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=sing,args=("再来一次", ))
    t2 = threading.Thread(target=dance,kwargs={"msg":"啦啦啦啦啦"})


    t1.start()
    t2.start()