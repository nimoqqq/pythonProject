"""
    把一组数据结构和处理它们的方法组成对象（object），
    把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，
    通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），
    通过多态（polymorphism）实现基于对象类型的动态分派
"""


class Student(object):
    # __init__ 是一个特殊方法用于在创建对象时进行初始化操作，类似于 java 中的构造函数
    def __init__(self, name, age, foo):
        self.name = name
        self.age = age
        self.__foo = foo  # 私有属性

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

    # 私有方法
    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38, 'hello')
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15, 'hello')
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
