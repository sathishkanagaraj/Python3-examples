#! python3
# regexes.py - will demonstrate how 're' module can be used for pattern matching

import re

def simplePhoneNumberMatch():
    phoneNumberpattern = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    search = phoneNumberpattern.search('This is my number 456-234-6548.')
    print('First group found %s'% search.group(1))
    print('Next group found %s'% search.group(2))
    print('whole group found %s'% search.group())

def pipecheck():
    batregex = re.compile(r'Bat(man|mobile|copter|bat)')
    batsearch = batregex.search('Batman lost a mobile')
    print(batsearch.group())
    print(batsearch.group(1))

def zeroOrOneWithQuestionMark():
    batregex = re.compile(r'Bat(wo)?man')
    optionalcheck1 = batregex.search('Batwoman has found her Batman')
    optionalcheck2 = batregex.search('Batman has found his Batwoman')
    print(optionalcheck1.group())
    print(optionalcheck2.group())

def zeroOrManyWithStar():
    batregex = re.compile(r'Bat(wo)*man')
    optionalcheck1 = batregex.search('Batwoman has found her Batman')
    optionalcheck2 = batregex.search('Batman has found his Batwoman')
    optionalmanycheck3 = batregex.search('Batwowowoman has found his Batman')
    print(optionalcheck1.group())
    print(optionalcheck2.group())
    print(optionalmanycheck3.group())

def oneOrMoreWithPlus():
    batregex = re.compile(r'Bat(wo)+man')
    check1 = batregex.search('Batwoman has found her Batman')
    check2 = batregex.search('Batman has found his Batwoman')
    manycheck3 = batregex.search('Batwowowoman has found his Batman')
    nonecheck4 = batregex.search('Batman has not found his BatWoman')
    print(check1.group())
    print(check2.group())
    print(manycheck3.group())
    print(nonecheck4 == None)

def matchwithrange():
    smileregex1 = re.compile('ho(ha){3}')
    smileregex2 = re.compile('ho(ha){3,5}')
    smileregex3 = re.compile('ho(ha){3,}')
    smileregex4 = re.compile('ho(ha){,2}')
    smilematch1 = smileregex2.search('hohahahahaha')
    smilematch2 = smileregex3.search('hohahahahahahahahah')
    smilematch3 = smileregex4.search('ho')
    print(smilematch1.group())
    print(smilematch2.group())
    print(smilematch3.group())

def findallthatmatches():
    batregex = re.compile(r'2{3}')
    optionalcheck1 = batregex.findall('122,222,223,222')
    print(optionalcheck1)

def matchOnlyNumbers():
    print(re.compile(r'\d').search('1234'))
    print(re.compile(r'\d{5}').search('There is a 5 digit number 12345 to be found'))
    print(re.compile(r'^\d+').search('123456789 has 9 digits'))
    print(re.compile(r'^\d+\s$').search('123456789 '))
    print(re.compile(r'\d{5}$').search('Five digit number at the end 12345'))

def wildcardmatch():
    wildcardmatches = re.compile(r'.at').findall('The cat in the hat sat on the flat mat.')
    print(wildcardmatches)
    wildcardmatches = re.compile(r'..at').findall('The cat in the hat sat on the flat mat.')
    print(wildcardmatches)
    ''' The dot represents characters , but start matches everything'''
    wildcardmatches = re.compile(r'I play (.*) and I Love (.*)').search('I play Football and I Love Tennis.')
    print(wildcardmatches.group())
    nongreedyregex = re.compile(r'.*?,').search('Betty bought some butter, but the butter was bitter, so betty bought some better butter, to make the bitter butter, butter better.')
    print(nongreedyregex.group()) # satisfied with first occurrence of ,
    greedyregex = re.compile(r'(.*,)(.*.)').search('Betty bought some butter, but the butter was bitter, so betty bought some better butter, to make the bitter butter, butter better.')
    print(greedyregex.group()) # greedy enough to look for all the occurrences of ,
    print(greedyregex.group(1))# first group
    print(greedyregex.group(2))# second group
    newlineexcludedregex = re.compile(r'.*').search('Betty bought some butter, \nbut the butter was bitter, \nso betty bought some better butter, \nto make the bitter butter, \nbutter better.')
    print(newlineexcludedregex.group())
    newlineincludedregex = re.compile(r'.*', re.DOTALL).search('Betty bought some butter, \nbut the butter was bitter, \nso betty bought some better butter, \nto make the bitter butter, \nbutter better.')
    print(newlineincludedregex.group())

def casematch():
    casesensitiveregex = re.compile(r'(Robocop)?')
    print(casesensitiveregex.search('RoboCop is a good movie').group())
    caseinsensitiveregex = re.compile(r'roboCoP', re.IGNORECASE)
    print(caseinsensitiveregex.search('RoboCop is a good movie').group())

def findreplace():
    findreplaceregex = re.compile(r'Lion (\w+)')
    print(findreplaceregex.sub('Cheetah', 'Lion is the fastest animal, Lion Wrong answer.'))
    hidecharregex = re.compile(r'my (\w)\w*')
    print(hidecharregex.sub(r'\1*****', 'my India is a my country'))


findreplace()