#这是一个很有趣，也很深入细致的关于decrator的例子

import time


def decrator(f):
    print("before:"+f.__name__+"called.")
    return f

def myfunc1():
    print("myfunc1() called")

@decrator
def myfunc2():
    print("myfunc2() called")

'''
执行顺序为：在执行decorator(myfunc1)()之前，会先执行@decorator
打印出：before:myfunc2called
'''
#下面是通过实践查看list的两种创建方式，哪个更快，用到decrator

def time_cost(f):
    start = time.clock()
    a = f()
    end = time.clock()
    print(f.__name__,"的执行时间为：",end-start)
    return a

@time_cost
def list_cmp():
    return [(x,y) for x in range(1000) for y in range(1000) if x*y > 25]

@time_cost
def for_loop():
    a=[]
    for x in range(1000):
        for y in range(1000):
            if x * y > 25:
                a.append((x, y))
    return a

#楼上是不带参数的decrator，楼下是带参数的decrator
def time_cost_decrator(f):
    print("in ",time_cost_decrator)
    def _f(*arg, **kwarg):
        start = time.clock()
        a=f(*arg,**kwarg)
        end = time.clock()
        print (f.__name__,"run cost time is ",end-start)
        return a
    return _f

@time_cost_decrator
def list_cmp_decrator(length):
    return [(x,y) for x in range(length) for y in range(length) if x*y > 25]

@time_cost_decrator
def for_loop_decrator(length):
    a=[]
    for x in range(length):
        for y in range(length):
            if x * y > 25:
                a.append((x, y))
    return a



if __name__ == '__main__':
    pass

    #@decrator会先执行
    # decrator(myfunc1)()
    # myfunc2()

    #两种创建list方式的时间比较
    # a = list_cmp
    # print(len(a))
    # a = for_loop
    # print(len(a))
    # 不加@time_cost时执行
    # a = time_cost(list_cmp)
    # a = time_cost(for_loop)

    #带参数的decrator
    #a = list_cmp_decrator(500)
    #a = for_loop_decrator(500)
