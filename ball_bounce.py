# 假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
# 最后的误差判断是小数点6位
import math
while True:
    try:
        height = int(input())
        length = height + height*(1-math.pow(0.5, 5-1))*2
        h5 = height/math.pow(2,5)
        # 先format保证六位小数的精度，再用float去掉尾部可能的多余的零
        print(float('{:.6f}'.format(length)))
        print(float('{:.6f}'.format(h5)))


    except:
        break