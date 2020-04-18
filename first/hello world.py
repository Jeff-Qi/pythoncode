import random
x = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
m = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
for i in range(100):
    X = random.choice(x)
    M = "".join(random.choice(m) for i in range(2))
    print(X+M)
