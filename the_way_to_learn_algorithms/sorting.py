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
#l[p:r]:待排序的数组
def merge_sort(l,p,r):
    '《算法导论》p17'
    if p<r:
        q=int((r+p)/2)
        merge_sort(l,p,q)
        merge_sort(l,q+1,r)
        #此时，l[p:q]和l[q+1:r]都已经排好序,即简单情况
        #但是为了能够在递归里使用这个函数，需要改的小细节很多，最主要的是
        #l是整个数组，遍历和写回原数组的时候，下标不能从0开始，而是p→r
        MERGE(l,p,q,r)

#这是归并排序的简单情况，楼上的方法用递归把问题分解成简单情况
#l:待排序数组，pqr是数组下标，p<q<r,假设l[p..q]和l[p+1..r]都已排好序
def MERGE(l,p,q,r):
    #两个数组的元素个数
    n1 = q-p+1
    n2 = r-q
    #新建两个数组,将l中的元素拷贝到这两个数组中
    A=list(l[p:q+1])
    R=list(l[q+1:r+1])
    #建立哨兵
    A.append(float("inf"))
    R.append(float("inf"))
    i = j = 0
    for k in range(p,r+1):
        #谁小，谁放回原数组中，然后index+1
        if A[i] < R[j]:
            l[k] = A[i]
            i += 1
        else:
            l[k] = R[j]
            j += 1
    return l


#快速排序
#这是《算法导论》里介绍的算法，取最后一个元素l[high]为 pivot element
def quick_sort(l,low,high):
    if low < high:
        q = PARTITION(l,low,high)
        quick_sort(l,low,q-1)
        quick_sort(l,q+1,high)
    return l

def PARTITION(l,p,r):
    key = l[r]
    #两个游标i，j。i指向最后一个值小于key的位置；j为遍历游标
    i = p-1
    j = p
    #开始找有多少个小于等于key的值，每找到一个i+1
    #这里要注意的是，j的遍历不包括r，因为最后遍历结束时，要把r上的值交换到i+1上
    while j < r:
        #找到一个
        if l[j] <= key:
            i+=1
            l[i],l[j] = l[j],l[i]
        j+=1
    #遍历结束
    l[i+1],l[r] = l[r],l[i+1]
    return i+1



#这是计算机408里的方法，但是《算法导论》里的方法不一样
#这里取第一个元素l[p]为 pivot element
#主要思想是，两个游标分别从两边向中间遍历，直至相等。
#参考快速排序百度百科
def quick_sort_408(l, p, q):
    low = p
    high = q
    if low >= high:
        return l
    key = l[low]
    while low < high:
        while low < high and l[high] > key:
            high -=1
        l[low],l[high] = l[high],l[low]
        while low < high and l[low] < key:
            low +=1
        l[low], l[high] = l[high], l[low]
    quick_sort_408(l, p, low - 1)
    quick_sort_408(l, high + 1, q)
    return l



if __name__ == '__main__':
    pass
    l = [13, 3, 2, 9, 1, 2, 0, 13, 6]
    list = [5,3,2,9,1,6,7,8]
    '快速排序'
    #计算机408的算法
    #print(quick_sort_408(list, 0, len(list) - 1))
    #《算法导论》的算法
    #print(quick_sort(list,0,len(list)-1))
    '归并排序'
    #简单情况
    #l1 = [2,4,5,7,1,2,3,6]
    #print(MERGE(l1,0,3,7))
    #一般情况
    #merge_sort(l, 0, len(l) - 1)
    #print(l)
    #
    '插入排序'
    # print(insert_sort(l))
    # print(insert_sort2(l))

    '选择排序测试'
    #print(select_sort(l))

    '冒泡排序测试'
    # print(bubble_sort(l))


