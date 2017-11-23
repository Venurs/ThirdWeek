class Music:

    __instance = None

    __first_init = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self, name):
        if self.__first_init:
            return

        self.name = name

        self.__first_init = True


mu = Music("够他")
mu1 = Music("")
print(mu.name)
print(mu1.name)
print(mu)
print(mu1)
