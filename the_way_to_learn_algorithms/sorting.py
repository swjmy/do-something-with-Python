#后面各种排序需要用到的，交换l数组中的x,y
def swap(x,y,l):
    l[x], l[y] = l[y], l[x]
    #可能你也发现了，python中swap操作很方便，不需要单独写一个函数
    #但是既然写了，就留下来当做笔记吧

#冒泡排序
def bubble_sort(l):
    for j in range(len(l),0,-1):
        for i in range(j):
             # 循环到最后一个
            if i == len(l) - 1:
                break
            # 排序结果为递增
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l

def select_sort(l):
    #这个min可以不设，然后每次假设第一个unsorted元素为min
    #为了方便理解，加了这个min变量，不影响复杂度
    min = l[0]
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if l[j] < l[i]:
                l[j],l[i] = l[i],l[j]
    return l

#插入排序
#这是《introduce to algorithms》书中的算法
def insert_sort(l):
    #和前几个排序算法一下，第一层遍历是为了区分sorted和unsorted
    #第一层的i指向桌子上的牌unsorted
    for i in range(1,len(l)):
        #从右往左遍历手里的牌，找到找到一个比extracted小的牌，插入
        extra = l[i]
        j = i-1
        while j >= 0 and l[j] > extra:
            l[j+1] = l[j]
            j = j -1
        else:
            l[j+1] = extra
    return l

#这是慕课网上一网友写的，稍有不一样。
def insert_sort2(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

#归并排序是典型的分治思想
#归并排序主要有两种实现方法：
#❤分解待排序的n个元素的序列成各具n/2个元素的两个字序列,
# 然后递归排序这两个序列，最终递归到每个序列的长度为1
#❤split each element into partitions of size 1。
# 将n个元素分成n个带归并的序列，最后归并成一个。
#你发现了，没错，这两种方法实际就是同一个，只是方法一用递归实现
def merge_sort(l):
    





if __name__ == '__main__':
    pass
    l = [13, 3, 2, 9, 1, 2, 0, 13, 6]
    '归并排序'

    '插入排序'
    # print(insert_sort(l))
    # print(insert_sort2(l))

    '选择排序测试'
    #print(select_sort(l))

    '冒泡排序测试'
    # print(bubble_sort(l))


