def checkdict():
    birthdays = {'Alice':'Jan 1', 'Bob':'Dec 5', 'Carol':'Oct 12'}

    while True:
        print('Please enter the name to find their birthday')
        name = input()
        if name == '':
            break

        if name in birthdays:
            print('%s birthday is on %s' %(name, birthdays[name]))
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday updated..')
            print(list(birthdays.values()))

def handleitems():
    birthdays = {'Alice':'Jan 1', 'Bob':'Dec 5', 'Carol':'Oct 12'}
    for k, v in birthdays.items():
        print('for key %s the value is %s'% (k,v))

def handledefault():
    message = ' I was born in July'
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] += 1
    print(count)

handledefault()