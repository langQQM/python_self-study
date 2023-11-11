def f(x,y,z):
    return x+y+z

print(f(1,2,30))

# 内置函数
print(len("money"))

# 必选及可选参数
def f(x=2):
    return x**x
print(f())
print(f(3))
print(f(4))


def add(x, y=10):
    return x+y

print(add(2))

