#!python3

from pathlib import Path
import os

def filebasics():
    formPath = Path('Users', 'sk', 'PythonProjects', 'Samples.txt')
    print(formPath)
    joinPath = Path('Users')/'sk'/'PythonProjects'
    print(joinPath)
    print(Path.cwd())
    print(Path.home())
    #os.makedirs(r'test/test1')
    print(joinPath.is_absolute())
    print(Path.cwd().is_absolute())
    isabspath = os.path.abspath(joinPath)
    print(os.path.isabs(isabspath))
    print(os.path.realpath('test2'))

    p = Path(r'/Users/sk/PythonProjects/Samples.txt')
    print(p.anchor)
    print(p.parent)
    print(p.name)
    print(p.stem)
    print(p.suffix)
    print(p.parents[1])
    print(p.parents[2])
    print('/usr/bin'.split(os.sep))

def fileaccesslevel1():
    print(str(os.path.getsize('/Users/sk/Downloads/ideaIU-15.0.6-custom-jdk-bundled.dmg')/(1024*1024)) +' mb')
    print(os.listdir('/Users/sk/Downloads/'))
    for item in list(Path('/Users/sk/Downloads/').glob('*.dmg')):
        print(item.name)

fileaccesslevel1()