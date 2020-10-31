class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}".format(self.name))

foo = Person()
bar = Person()
foo.set_name('Luke Skywalker')
bar.set_name('Anakin Skywalker')
foo.greet()
bar.greet()

print(foo.get_name())

class Bird:
    song = 'Squaawk'
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()

birdsong = bird.sing
birdsong()

bsong = bird.sing()
# bsong

class Class:
    def method(self):
        print('I have a self!')

def function():
    print("I don't...")

instance = Class()
instance.method()
instance.method = function
instance.method()

#要让方法或属性成为私有的（不能从外部访问），只需让其名称以两个下划线打头即可。
class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me...")
    
    def accessible(self):
        print('The secret message is:')
        self.__inaccessible()
s = Secretive()
# s.__inaccessible
s.accessible()

class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

f = Filter()
f.init()
f.filter([1, 2, 3])
print(f.init())
print(f.filter([1, 2, 3]))

print(issubclass(SPAMFilter, Filter))

#如果你有一个类，并想知道它的基类，可访问其特殊属性__bases__。
print(SPAMFilter.__bases__)

#要确定对象是否是特定类的实例，可使用isinstance。
print(isinstance(SPAMFilter, Filter))

