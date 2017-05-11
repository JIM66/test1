# 自定义函数Hello
def hello(name):
    return 'hello,'+name+'!'

# 自定义函数Fibs
def fibs(num):
    result = [0, 1]
    if num == "":
        print("please input num")
    for i in range(num):
        result.append(result[-2]+result[-1])
    return result

print(fibs(5))
