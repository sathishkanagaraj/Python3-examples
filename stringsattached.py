multiline = '''Dear Sir,
How are you?
Where have you been?
Hope you are doing Good!!
'''

escapechar = 'She\'s the man \nGladiator \nOne flew over the cuckoo\'s neat'

escapeusingrstring = r"She's the man / Gladiator / One flew over the cuckoo's nest"

eclist = escapechar.split('\n')

'''
The below code works for f-strings but IDEA15 does't support
for i in range(1,10):
    print(f'wewer{i}')
'''

for each in eclist:
    print(each.ljust(50,'.'))


for each in eclist:
    print(each.center(50,'.'))

print(multiline)
print(escapechar)
print(eclist)