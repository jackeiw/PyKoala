#迭代使用
#获取最大最小值
def findMinAndMax(x):
    if not isinstance(x, list):
        raise TypeError('Invalid')
    x_num = [c for c in x if type(c) is int]
    if len(x_num) == 0:
        return (None, None)
    min = x[0]
    max = x[0]
    for i, num in enumerate(x):
        if num > max:
            max = num
        elif num < min:
            min = num
    return (min, max)

''' 
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''


