class Dog():
    """一次模拟小狗的简单尝试"""

    # 公有变量
    publicAttr = 'xiao'
    # 保护变量
    _protectedAttr = 12
    # 私有变量
    __privateAttr = 'rao'

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

    @classmethod
    def class_method(cls):
        '''类方法'''
        print('类方法')

    @staticmethod
    def static_method():
        '''静态方法'''
        print('静态方法')

    def __del__(self):
        '''析构函数'''

##########################################################
# __init__ 构造函数，self第一个参数
#
# self在定义的时候要写进去，在调用的时候则不需要传入
#
# 类中的每个属性都必须有初始值

##########################################################

# 类的继承
#
# 显示的继承，注意构造函数的写法
#
# 在子类中定义新的属性
#
# 在子类中重写父类的方法，方法名相同就算重写，参数部分可以相同可以不同


class Hashiqi(Dog):
    """哈士奇"""

    def __init__(self, name, age):
        super().__init__(name, age)
        self.sex = 1

    def sit(self, where):
        """哈士奇蹲下"""
        print("Hashiqi "+self.name.title() + " is now sitting "+where)

    def eat(self):
        """哈士奇吃东西"""
        print("Hashiqi "+self.name.title() + " is now eatting.")

    def __enter__(self):
        print('上下文管理器-enter')

    def __exit__(self, *args):
        print('上下文管理器-exit')


'''
上下文管理器：一个类实现了 __enter__ 和 __exit__，就满足了上下文管理器，就可以使用 with 语句来调用，比如我们打开文件时的操作，
在开始的时候会调用 __enter__ ，在结束的时候会调用 __exit__，分别用来做初始化操作和资源清理操作。
'''
