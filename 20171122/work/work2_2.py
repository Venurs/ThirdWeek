"""创建父类植物类，属性：名称。方法：显示属性信息。
创建两个子类：花和草。分别新增属性和功能。测试代码。
"""


class Paint:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)


class Folwer(Paint):

    # def __init__(self, name, nature):
    #     super(Folwer, self).__init__(name)
    #     self.__nature = nature

    def get_nature(self):
        return self._nature

    def set_neture(self, nature):
        self._nature = nature

    nature = property(get_nature, set_neture)


class Grass(Paint):

    def __init__(self, name, funcation):
        super(Grass, self).__init__(name)
        self.__funcation = funcation

    def get_funcation(self):
        return self.__funcation

    def set_funcation(self, funcation):
        self.__funcation = funcation

    function = property(get_funcation, set_funcation)


pa = Paint("土豆")
print(pa.name, end=" ")
pa.name = "红薯"
print(pa.name)

fo = Folwer("紫藤萝")
print(fo.name, end=" ")
# fo.nature = "好看"
print(fo.nature)

gr = Grass("龙葵", "常见")
print(gr.name, end=" ")
# gr.function = "草药"
print(gr.function)

