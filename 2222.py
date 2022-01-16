# str='-'
# ss=('1','2','3')
# yy=str.join(ss)
# print(yy)
# #str(ss)
# import time  # 引入time模块
#
# ticks = time.time()
# print ("当前时间戳为:", ticks)
# print(type(ticks))
# l1=[1,22,33,22,22,44,55]
# ll='abcdefg'
# print(ll.index('a',0,4))
# print(ll.find('a',0,5))
# print(l1.count(22))
# ls=[1,2,3,4,'aa']
# ls.append(['pp',332])
# ls.append(['pp',33])
# print(ls)
# ls.insert(2,'222')
# print(ls)
# ls.extend([4,666,777])
# ls.remove(['pp',332])
# ls.remove(['pp',33])
# ls.remove('aa')
# ls.remove('222')
# print(ls)
# # ls.pop(1)
# # print(ls)
# # ls.remove(['pp', 33])
# # print(ls)
# ls.reverse()
# print(ls)
# ls.sort()
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# list1 = [23,54,56]
# list2 = list1
# list2[1] = 100
# print(list1)
# print(list2)
# print(id(list1) == id(list2))
#
# list1 = [23,54,56]
# list2 = list1.copy()
# list2[1] = 100
# print(list1)
# print(list2)
# print(id(list1) == id(list2))

# t3 = list('abcd')
# print(type(t3))
# print(t3)

# !/usr/bin/python3

# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# for jj in f:
#     print(jj)
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
s = 'name'
year = 10
print('it is %s,and it is %d old' % (s, year))

print(f'it is {s},and it is {year} old')

print('it is {1},and it is {1} old'.format('s', 'year'))
