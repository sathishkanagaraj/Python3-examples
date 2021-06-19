
def simplelisttest():
    fruits = ['apple', 'Guava', 'banana', 'Papaya']
    print('The fruit starts with letter "b" is %s'% (fruits[2]))
    print('The first three fruits are %s'% (fruits[2:5]))
    print('The last fruit is %s'% (fruits[0:-2]))
    print('The complete fruits are %s'% (fruits[:]))
    print('The fruits listed until 2 are %s'% (fruits[:2]))
    print('The fruits listed from 2 are %s'% (fruits[2:]))
    print('The fruits length -  %s'% (len(fruits)))

def listconcat():
    wildAnimals = ['lion', 'tiger', 'giraffe', 'cheetah', 'hippopotamus']
    domesticAnimals = ['cow', 'goat', 'donkey', 'horse']
    print(wildAnimals+domesticAnimals)
    for index, animal in enumerate(wildAnimals+domesticAnimals):
        print('Index %s for animal %s' %(index, animal))

def appendremovedelinsert():
    fruits = ['apple', 'Guava', 'banana', 'Papaya']
    fruits.append('pomegranate')
    print(fruits)
    fruits.sort(reverse=True)
    print(fruits)
    fruits.sort(key=str.lower)
    print(fruits)
    fruits.reverse()
    print(fruits)
    fruits.remove('apple')
    print(fruits)
    del fruits[3]
    print(fruits)
    print(type(fruits))
    fruits = ('strawberry')
    print(type(fruits))
    fruits = ('strawberry',)
    print(type(fruits))

def listtupletoggle():
    domesticAnimals = ['cow', 'goat', 'donkey', 'horse']
    print(tuple(domesticAnimals))
    print(list(tuple(domesticAnimals)))
    print(list(domesticAnimals[-1]))

def immutabletuple():
    carsTuple = ('santro', 'brio')
    #kindly try deleting or removing which is not possible
    print(carsTuple)

immutabletuple()