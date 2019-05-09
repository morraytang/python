#（*） 星号的参数传递主要是在不知道参数多少的情况下可以准确的传递参数

# usage of  * and zip
u1 = [2,4,6]
u2 = [3,5,7]

for m, n in zip(u1,u2):
    print(m,"-",n)

#当方法参数个数不定的时候，* 类似一个列表
def multiple(arg, *args):
    print("arg: ", arg)
    #打印不定长参数
    for value in args:
        print("other args:", value)

#在Python数学运算中*代表乘法，**为指数运算
print(2*4)
print(2**4)



#下面主要说一下参数收集的逆过程，也就是方法定义中并没有星号，但是在调用方法的时候携带了星号作用是什么？
#可见在调用参数的时候使用*号可以将元组（一个整个）解包成一个列表（多个值）
# #同理如果是两个星号的话，就是带有**号的字典，自动解包
def add(x,y):
    return x + y
paras = (1,2)
paras2 = {"x": 3,"y":6}
print("sum is : ",add(*paras))
print("sum is : ", add(**paras2))



if __name__ == '__main__':
  multiple(1,'a',True)