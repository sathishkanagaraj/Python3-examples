#! python 3
# phomailproject.py , helps to identify phone number and email in a specific format
# use test.txt to copy(load the clipboard)

import pyperclip, re

phoneregex = re.compile(r'(\d{3})?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|X|ext.)\s*(\d{2,4}))?')
emailregex = re.compile(r'([a-zA-Z0-9.+_%-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')

def checkphonenuber():
    print(phoneregex.search('456-7896').group())
    print(phoneregex.search('235-458-2356').group())
    print(phoneregex.search('011.789.6358    X    11').group())

def checkemail():
    print(emailregex.search('rocky%balboa@rocky.com').group())
    print(emailregex.search('rocky.bal_boa@rocky.balboa.com').group())

#checkphonenuber()
#checkemail()

fromclipboard = str(pyperclip.paste())
matches = []
for phngroups in phoneregex.findall(fromclipboard):
    phnumber = '-'.join([phngroups[0], phngroups[2], phngroups[4]])
    matches.append(phnumber)

for emailgroups in emailregex.findall(fromclipboard):
    matches.append(emailgroups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
    print('Copied to Clipboard')
