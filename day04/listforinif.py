#!/usr/bin/env   python
import  keyword
print(keyword.kwlist)

# 遍历key值，value值（下面写法完全等价）：
a = {'a': '1', 'b': '2', 'c': '3'}
for key in a:
    print(key+':'+a[key],sep=' -- ',end=' $')

print('directory 方式一 for key in a')

for key in a.keys():
    print(key+':'+a[key],sep=' -- ',end=' $')

print('directory 方式2 for key in a.keys()')

for key,value in a.items():
       print(key+':'+value,sep=' -- ',end=' $')

print('directory 方式3 for key,value in a.items()')


for (key,value) in a.items():
    print(key+':'+value,sep=' -- ',end=' $')

print('directory 方式4 for (key,value) in a.items()')



#在for 循环中,遍历元组的每一项
mytuple = ('yuanzu',111,True,('ziyuan',11.002))
print('mytuple is ',mytuple)

for value in mytuple:
  print('tuple value type is ',value,type(value))


#使用for...in语句遍历列表中的元素
mylist = ['a0',11,False,['aa0',True,22]]
print('mylist is %s' % mylist)
for value in  mylist:
  print('list value type is ',value,type(value))

getlist = ['%s\n' % element for element in mylist]
print('getlist is  %s ' % getlist)

intlist = [1, 2, 3, 4, 5]
print('intlist is %s' % intlist)

#每个列表元素的二次方
get_intlist = [element ** 2 for element in intlist ]
print('get_intlist is %s' % get_intlist)


#找出30以内的能够被3整除的正整数
int3list = [element for element  in  range(1,30) if  element % 3 == 0 ]
print('The positive integer divided by three is \n %s' % int3list)


tplist = ['a0',11,False,['aa0',True,22],('tuple-element',100,['cc00',1.002])]
print('tplist is %s' % tplist)
#内置函数enumerate 实现功能:同时得到元素编号和元素
for (index,value) in  enumerate(tplist):
  print('index is %d value is %s  type value is  %s' % (index,value,type(value)))


