# python

```bash
python --version
pip --version
pip install virtualenv #install virtualenv
mkdir workspace
cd workspace
pwd

#create virtualenv
virtualenv venv
#enter virtualenv
source venv/bin/activate
#exit virtualenv
deactivate
```

# vi
```
#종료
:q
#강제종료
:q!
#저장
:w
#저장하고 끝내기
:wq
# insert
i
# append
a
# delete char
x
# delete line
dd
# delete word
dw
# insert line upper
O
# insert line lower
o
# copy single line
yy
# copy 4 lines
4yy
# paste to upper
P
# paste to lower
p
# move to the first line
1G
```
`~/.vimrc` (mac)
```
syntax on
se expandtab sw=4
```

# project 1011_lecture.py

```
(venv) $ pip install opencv-python
```

#### port 
default web port: 80  
telnet: 21  
ssh: 22  

devport: 8888

#### ip address
```bash
# mac ipaddress
ifconfig
```

# project 1011_lecture.py windows

#### install git bash
turn off windows explorer integration
use git from git bash only
checkout as-is commit as-is

##### anaconda path
c:\programdata\anaconda2
c:\programdata\anaconda2\Scripts

#### virtualenv
```bash
mkdir workspace
cd workspace
pip install virtualenv
virutalenv venv
# in git bash windows
source venv/Scripts/activate
which python
```

#### parallel network
mac --- parallel (service)
parallels -> right-click -> 환경설정 -> 네트워크 -> port forwarding


# install python 3.6 on mac mojave

```bash
brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb --foce-bottle
```

venv
```
python3 -m venv venv
source venv/bin/activate
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ4NzEwMTg5NSwtMTc3MzM5MTc2OSwxOT
I1Njg1NjQ3LDYwNTg5NTk4MiwtMTU0ODI5OTcxNiwtMTcyNzUw
NDgzNSwtMTM2NTAwNTIxMiwtMTYxNTMyMjE2NSwyMDI4ODkwNz
Y0LC0yMTAzMTMyMjExLDIwNDc1MDMwNjcsMTYzNTQ4ODM3Miwt
Mjg5OTU4OTgsMTM2NjQ2NTcyNSwtNzc3NTI2MDQ1LDE4NTc5MD
YwMDcsNDg4OTU0Njg5LC0xMjQzMDQ0ODA5LC02MzM1NDA3NzQs
MTE2MzY4Nzc4M119
-->