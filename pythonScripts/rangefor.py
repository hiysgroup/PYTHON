#!/usr/bin/env  python3
import  random
import  getpass

for  character  in  "ab":
  print(character,type(character))
  print('-' * 10)

for  tuple  in (10, [-30,'abc',False]):
  print(tuple,type(tuple))
  print('$' * 10)

for  listx  in ['belle' , 'beauty']:
  print(listx,type(listx))
  print('#' * 10)

directory =  { 11: 110, 'man': False}
for  key  in  directory:
  print(key,type(key))
  print(key," : ",directory[key])
  print('&' * 10)

print(range(3))
list
#del list
lx = list(range(3))
print(lx)
for  i  in  lx:
  print(i)

L = list(range(20))
print(L)
#取前三个数据
print(L[0:3])
#取下标1-3条数据
print(L[1:3])
#取倒数第一条数据
print(L[-1:])
#取倒数1-2条数据
print(L[-2:])
#每隔两个取一条数据
print(L[::2])
#前6个数据，每隔三个去一条
print(L[:6:3])
#复制一个list
print(L[:])

print("**list(range(3,6))***" * 2)
print(list(range(3,6)))

print("****list(range(1,10,2))*" * 2)
print(list(range(1,10,2)))

print("********list(range(0,11,-2))**" * 2)
print(list(range(0,11,-2)))
