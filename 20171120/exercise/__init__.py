# def strong(fun):
#     def new_fun():
#         print("zhngshiqi ")
#         fun()
#     return new_fun
#
#
# @strong
# def fun():
#     print("原始函数")
#
#
# fun()

choose = int(input())


def strong(fun):
    if choose == 1:
        def new_fun():
            print("新函数1")
            fun()
    elif choose == 2:
        def new_fun():
            print("新函数2")
            fun()
    elif choose == 3:
        def new_fun():
            print("新函数3")
            fun()
    return new_fun


def strong1(fun):
    def new_fun1():
        print("装饰器2")
        fun()
    return new_fun1


@strong1
@strong
def fun():
    print("原始函数")


fun()