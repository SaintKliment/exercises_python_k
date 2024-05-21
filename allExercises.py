#1
# c_lst = []
# for i in range(10):
#     c_lst.append(i)
# c = tuple(c_lst)
# for i in c:
#     print(i)

#2
# lst = list()
# for i in range(20):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)

#3
# s = str(input("input your str: "))
# lst = s.split()
# se = set(lst)
# print(se)

#4
# lst = [1, 2 ,3 ,4 , 5]
# s = 0
# for i in lst:
#     s += i
# print(s)

#5
# max = 0
# min = 1000000000000000
# lst = [-1, -2, -3, -4, 1, 2, 3, 4]

# for i in lst:
#     if max < i:
#         max = i
#     if min > i:
#         min = i
# print(max, min)

#6
# lst = [1, 2,-1, -2, -4, -3, 3, 4]
# lst_ = []
# for el in lst:
#     if el < 0:
#         index = lst.index(el)
#         lst.pop(index)
#         lst.insert(index, 0)
#         # 
# for i in lst:
#     if i > 0:
#         lst_.append(i)
# print(lst_)

#7
# lst = [1 ,2 ,3 ,4]
# lst_2 = []
# for i in lst:
#     a = i * i
#     lst_2.append(a)
# print(lst_2)

#8
# lst = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
# index = 0
# definite = 1
# for i in lst:
#     if definite == i:
#         print(index)
#     index += 1

#9
# lst = [1, 2, 3, 4, 5]
# for i in lst:
#     if i % 2 == 0:
#         print("yes")
#         break

#10
# lst = [1, 2, 3, 4, 5]
# f = lst.pop(0)
# l = lst.pop(-1)
# lst.append(f)
# lst.insert(0, l)
# print(lst)

# 11
# lst = list()
# st = "1"
# for i in range(10):
#     lst.append(st)
#     st += str(i)

# for i in lst:
#     if len(i) > 5:
#         print(i)

#12
# lst = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
# print(set(lst))

# 13
# lst = []
# for i in range(100):
#     lst.append(i)

# j = 0
# a = 'Fizz'
# b = 'Buzz'
# c = 'FizzBuzz'

# for i in lst:
#     if i % 3 == 0:
#         lst.pop(j)
#         lst.insert(j, a)
#     if i % 5 == 0:
#         lst.pop(j)
#         lst.insert(j, b)
    
#     if i % 5 == 0 and i % 3 == 0:
#         lst.pop(j)
#         lst.insert(j, c) 

#     j += 1

# print(lst)

# 14
# import random

# lst = []
# for i in range(10):
#     lst.append(random.randint(0, 100))
# lst.sort(reverse=True)
# print(lst)

# 15
# import random
# lst = []
# lst_1 = []

# for i in range(10):
#     lst.append(random.randint(0, 100))

# for n in lst:
#     if n <= 1:
#         break
#     d = 2
#     while d * d <= n and n % d != 0:
#         d += 1
#     if (d * d > n):
#         lst_1.append(n)
# print(lst_1) 

# 16
# lst = []
# a = '1'
# for i in range(10):
#     lst.append(a)
#     a += str(i)
    
# lst.insert(0, '123123123')
# lst.sort()
# print(lst)

# 17
# import random
# lst = []
# for i in range(10):
#     lst.append(random.randint(10, 100))

# for i in lst:
#     s = str(i)
#     if s == s[::-1]:
#         print(s)

# 18
# import random
# lst = []
# for i in range(10):
#     lst.append(random.randint(-100, 100))

# j = 0
# for i in lst:
#     if i < 0:
#         lst.pop(j)
#         lst.insert(j, 0)
#     j += 1
# print(lst)

# 19
# l = 'a'
# lst = ['asd', 'das', 'dos', 'ddos', 'frod', 'frog', 'kernel', 'non-kernel', 'rootkit']
# for i in lst:
#     if i[0] == l:
#         print(i)

# 20
# lst_ = list()
# lst = [1, 1, 2, 4, 5, 25, 1, 2, 3, 4, 5, 6]
# for i in lst:
#     for j in lst:
#         if i**0.5 == j:
#             lst_.append(i)
# print(set(lst_))
 
# 21
# import random
# lst = [random.randint(-100, 100) for i in range(10)]
# c_1 = 0
# c_2 = 0
# for el in lst:
#     if el > 0:
#         c_1 += 1
#     if el < 0:
#         c_2 += 1
# print(c_1, c_2)

# 22
# import random
# lst_ = list()
# lst = [random.randint(-100, 100) for i in range(10)]
# for i in lst:
#     if i % 7 == 0:
#         lst_.append(i)
# print(lst_)

# 23 
# lst = ['ээ', 'абв', 'где', 'здесь']
# lst.sort()
# print(lst)

# 24
# lst = [ 123, 1237, 3127, 754, 534, 25]
# for i in lst:
#     str_ = str(i)
#     for l in str_:
#         if l == '7':
#             print(i)

# 25
# from re import sub
# str_ = 'ячсмпаийбьцуьйтеп'
# print(sub(r"[яиюэоаыуе]", "*", str_))

# 26
# import random
# sum = 0
# lst = [random.randint(0, 100) for i in range(10)]
# for s in lst:
#     str_ = str(s)
#     for i in str_:
#         n = int(i)
#         sum += n
#     if sum > 10:
#         print(s)
#     sum = 0

# 27
# lst = ['Python i love you', 'Python is not Assembler for you', 'chair car var', 'let const useState']
# for s in lst:
#     lst_str = s.split()
#     for i in lst_str:
#         if i == 'Python':
#             print(s)

#28
# import random
# lst = [random.randint(0, 100) for i in range(10)]
# for i in lst:
#     s = str(i)
#     if s[-1] == '3':
#         print(i)

# 29
# se = set()
# lst = ['mbheqwq12', '12hvg3', 'sjfbosf', 'sdkfnshdf', 'hb32jk']
# for e in lst:
#     for i in e:
#         try:
#             int(i)
#             se.add(e)
#         except ValueError:
#             continue
# print(se)

#30
# import random
# lst = [random.randint(0, 10) for i in range(10)]
# c = 0
# for i in lst:
#     if i % 2 == 0:
#         lst.pop(c)
#         l = i * i
#         lst.insert(c, l)
#     c += 1
# print(lst)