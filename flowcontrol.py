# looping
import random

import sys


def dowhile():
    name = ''
    while name != 'sathish':
        print('please type sathish')
        name = input()
    print('Got u...')


def dobreak():
    while True:
        name = input()
        if name == 'sathish':
            break

    print('out of the loop')


def docontinue():
    while True:
        print('Who are you?')
        name = input()
        if name != 'Joey':
            continue
        print('Hi Joey, What is the password?')
        password = input()
        if password == 'password':
            break
    print('Access granted')

def dofor():
    for i in range(10,20,2):
        if i == 16:
            break
        print('num = '+str(i))

def doreversefor():
    for i in range(10,-5,-2):
        print('num = '+str(i))


def dorandom():
    while True:
        print('Guess a number..')
        randomvalue = random.randint(1,10)
        if int(input()) == randomvalue:
            print('Your input %d and random value %s matched' % (randomvalue,randomvalue))
            sys.exit()
        print('Try another number..')

dorandom()
