#用递归的方法实现反转字符串
#当然直接用切片可能实现，但是这里的分治的思想很不错
def reverse_str(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_str(s[1:])+s[0]

s = "ilikepython"

#二分法求平方根
#small为精度范围
def sqrt_func_dg(x,low,high,small=1):
    #猜测一个值，这个值去平均值
    guess = float(low+high)/2
    #计算猜测值得结果
    guess_square = guess**2
    #根据对结果的验证，做矫正
    #如果结果小于精度范围，计算完成，返回结果
    if abs(guess_square-x)<small:
        return guess
    #如果结果大于x的值，说明猜测值大了
    elif guess_square>x:
        return sqrt_func_dg(x,low,guess,small)
    #如果结果小于x的值，说明猜测值小了
    elif guess_square<x:
        return sqrt_func_dg(x,guess,high,small)

#作业：二分法完成插入
def bisection_insert(x,list,low,high):
    #x比最小的小
    if x<list[0]:
        insert_list(x,0,list)
        return
    #x比最大的大
    elif x>list[list.__len__()-1]:
        list.append(x)
        return
    #x在中间
    mid = int((low+high)/2)
    #mid 一直替换 low 的结果,则mid所指的值比x小
    if low == mid or list[mid] == x:
        insert_list(x,mid+1,list)
    #mid 一直替换 high 的结果，则mid所指的值比x大
    elif high == mid:
        insert_list(x,mid,list)
    elif list[mid] > x:
        return bisection_insert(x,list,low,mid)
    elif list[mid] < x:
        return bisection_insert(x,list,mid,high)



#插入列表操作
def insert_list(x,index,l):
    l.append(0);
    for i in list(range(index,len(l)))[-2::-1]:
        l[i+1] = l[i]
    l[index] = x



if __name__ == '__main__':
    pass
    '作业：二分法插入数组'
    l = [1,2,3,4,6,7,8]
    bisection_insert(9,l,0,len(l))
    print(l)
    '测试插入列表操作'
    # l = [1,2,3,4,5,6]
    # insert_list(0,3,l)
    # print(l)
    '测试二分法求平方根'
    #print(sqrt_func_dg(10,0,10,0.1))
    '递归法反转字符串'
    #print(reverse_str(s))