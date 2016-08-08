import random

import functools


def getLower():
    return lambda x,y:x if x<y else y

def sortedRandint():
    lst = [random.randint(-50,50) for i in range(10)]
    lst2 = filter(lambda n:n>0,lst)
    lst3 = map(lambda x:x*2,lst)
    #cmp的结果>0， 则将x放后面
    #这是python2的写法，如果在py3中用这种方法，需要把原来的cmp转换成key
    c = sorted(lst,key = functools.cmp_to_key(lambda x,y:x-y))
    #如果不写lambda，默认递增排序
    #和楼上类似如果lambda结果=1，则将x放后面
    lst.sort(key = functools.cmp_to_key(lambda x,y:1 if x>y else -1))
    return lst3

def sorted_str(s):
    #过滤掉非字母字符
    a = list(filter(str.isalpha,s))
    #对字符串进行排序
    b = sorted(a,key = functools.cmp_to_key(lambda x,y:1 if (x.upper()>y.upper()) else -1))
    a.sort(key= functools.cmp_to_key(lambda x,y:1 if (x.upper()>y.upper()) else -1))
    print("".join(a))
    print("".join(b))


if __name__ == '__main__':
    sorted_str("aAsmr3idd4bgs7Dlsf9eAF")