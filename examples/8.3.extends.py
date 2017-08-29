#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')


# 继承 Animal
class Dog(Animal):
    # 子类方法覆盖父类方法
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog Eating meat...')


# 继承 Animal
class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()


# 检查某个变量是否某个类型 `isinstance()`
print(isinstance(dog, Dog))    # True

print(isinstance(cat, Cat))    # True

print(isinstance(dog, Animal)) # True


# 多态
def run_twice(animal):
    animal.run()
    animal.run()

# 多态的好处如下
run_twice(Animal()) # Animal is running...

run_twice(Dog())    # Dog is running...

run_twice(Cat())    # Cat is running...
