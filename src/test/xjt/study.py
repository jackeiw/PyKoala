# 导入 random(随机数) 模块
import random

#a=random.randint(0,9)
#print(str(a))

man = 0
count = 0
while count < 10:
    man = random.randint(0, 1000) # 取0~1000的随机数，可以先不管
    # print('一条好汉出生了：'+str(man))
    count = count + 1
    if count >= 10: # 过了10次机会不没了
        break
    if man > 100 and man % 3 == 0 and man % 5 == 0 and man % 2 == 0: # 愿意为你死
        break

if count < 10:
    print('Goodbye! 经过' + str(count) + '次碰撞，他 ['+ str(man)+'] 来了。祝你和' + str(man) + '幸福~')
else:
    print("注定孤独终老， o(╥﹏╥)o")


while True:  # 该条件永远为true，循环将无限执行下去
    num = input("Enter a number  :") # 输入一个数
    print("You entered: ", num)
    if num > 100:
        break

print("Good bye!")