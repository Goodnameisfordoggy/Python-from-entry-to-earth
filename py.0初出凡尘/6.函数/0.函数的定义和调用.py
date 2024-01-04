"""
#函数的定义和调用
  创建函数的目的是封装业务逻辑,实现代码的重用.
   #创建函数的关键字:def
     注意:现定义函数,再调用函数
   #函数的参数
(在次之前,针对各类对象调用的非常多的函数,这些都是Python的内建函数.
这些函数的功能都是预先设计好的,但在实际生产过程中,使用最多的还是自定义函数)
"""
#使用常量
 #创建函数
def aaa():
    print("I love you")
 #运行函数
aaa()    # I love you

#使用变量
 #创建函数
def bbb(a):# 创建函数时使用的变量a为形参
    print(a)
bbb("我爱你")# 调用函数时传递的是实参    #我爱你


#e.g求两个数和的函数
def ccc(a, b):
    print(a+b)
ccc(10, 20)    # 30
ccc(600, 66)   # 666
