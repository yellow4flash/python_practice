# class A:
#     def __init__(self,v):
#         self.__a=v+1

# a=A(0)
# print(a.__a)
# class A:
#     def __init__(self,v=1):
#         self.v=v
#     def set(self,v):
#         self.v=v
#         return v
# a=A()
# print(a.set(a.v+1))
# class A:
#     X=0
#     def __init__(self,v=0):
#         self.Y=v
#         A.X+=v

# a=A()
# b=A(1)
# c=A(2)
# print(c.X)
# class A:
#     def __init__(self):
#         pass

# a=A(1)
# print(hasattr(a,'A'))
# class A:
#     def __str__(self):
#         return 'a'
# class B(A):
#     def __str__(self):
#         return 'b'
# class C(B):
#     pass
# o=C()
# print(o)
# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))
# class Ex(Exception):
#     def __init__(self,msg):
#         Exception.__init__(self,msg+msg)
#         self.args=(msg,)
# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)

# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.i==len(self.s):
#             raise StopIteration
#         v=self.s[self.i]
#         self.i+=1
#         return v
# for x in I():
#     print(x, end="")

# def I(n):
#     s='+'
#     for i in range(n):
#         s+=s
#         yield s
# for x in I(2):
#     print(x, end='')
# def o(p):
#     def q():
#         return'*'*p
#     return q

# # r=o(1)
# # s=o(2)
# # print(r()+s())
# # import math
# # print(dir(math))
# print(__name__)
# try:
#     raise Exception
# except BaseException:
#     print('a')
# except Exception:
#     print('b')
# except:
#     print('c')
# x="\\\"
# print(len(x))
#! testear
# for x in open('file','rt'):
#     print(x)
# str='abcde'
# del str[2]
# print(str)
# print(len((1,)))
# d={'uno':1,'tres':3,'dos':2}
# for k in sorted(d.values()):
#     print(k, end=' ')
# print(len([i for i in range(0, -2)]))
# i = 4
# while i>0:
#     i-=2
#     print("*")
#     if i==2:
#         break
# else:
#     print("*")
# t=(1,2,3,4)
# t=t[-2:-1] #no toma el ultimo valor
# t=t[-1]
# print(t)
# d={}
# d['2']=[1,2]
# d['1']=[3,4]
# print(d)
# def fun(d,k,v):
#     d[k]=v
# dc={}
# print(fun(dc,'1','v'))
# for c in range(2):
#     print(c)
# class A:
#     def __init__(self,name):
#         self.name=name
# a=A("class")
# print(a)

# x="""
# """
# print(len(x))

# class A:
#     def __init__(self):
#         pass
#     def f(self):
#         return 1
#     def g():
#         return self.f()
# a = A()
# print(a.g())