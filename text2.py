#装饰器
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner


#装饰器普通写法
def sleep():
    import random
    import time
    print("Sleeping...")
    time.sleep(random.randint(1,5))


fn = outer(sleep)
fn()




#装饰器的语法糖写法
@outer
def sleep():
    import random
    import time
    print("Sleeping...")
    time.sleep(random.randint(1,5))

sleep()

