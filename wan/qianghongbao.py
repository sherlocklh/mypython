import random
import sys
def calRandomValue(total, num):
    total = float(total)
    num = int(num)
    min = 0.01 #基数
    if(num < 1): 
        return
    if num == 1:
        print ("第%d个人拿到红包数为：%.2f" %(num, total))
        return
    i = 1
    while( i < num ):
        max = total - min*(num- i)
        k = int((num-i)/2)
        if num -i <= 2:
            k = num -i
        max = max/k
        monney = random.randint(int(min*100), int(max*100))
        monney = float(monney)/100
        total = total - monney
        print ("第%d个人拿到红包数为：%.2f, 余额为: %.2f" %(i, monney, total))
        i += 1
    print ("第%d个人拿到红包数为：%.2f, 余额为: %.2f" %(i, total, 0.0))
if __name__ == "__main__":
    total = input('输入红包总金额:')
    num = input('输入发红包数量:')
    calRandomValue(total, num)