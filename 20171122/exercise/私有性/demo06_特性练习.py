class Student:

    def __init__(self, name):
        self.name = name

    # 赋值
    def set_score(self, score):
        if score < 0 or score > 100:
            print("成绩有误")
            self._score = 0
        else:
            self._score = score
    # 取值
    def get_score(self):
        return self._score

    score = property(get_score, set_score)

s1 = Student("王二狗")
s2 = Student("李小花")
s1.name = "王三狗"  # 对象.属性 = 赋值

s1.set_score(88)

s1.score = -88  # 对象.属性= 赋值 --- >对象.特性--- >方法：set
print(s1.score)


"""
方法一：
    特姓名= property(get_score,get_score)
方法二：
    装饰器：@property，@特姓名.setter,
            @特姓名.getter,@特姓名.deleter
"""