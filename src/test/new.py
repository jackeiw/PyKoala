#获取最大最小值
def findMinadnMax(x):
    if x.length < 1:
        return (None, None)
    else:
        min = max= x[0]
        for num in x:
            if num > max:
                max = num
            else:
                min = num
        return (min, max)

    # 测试
    if findMinadnMax([]) != (None, None):
        print('测试失败!')
    elif findMinadnMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinadnMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinadnMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
