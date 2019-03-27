#!/usr/bin/env  python3

#cock公鸡 + hen母鸡 + chick小鸡 = 100
#5 * cock + 3 * hen + z/3 = 100
import  time, datetime
#时间模块  time.time()函数

localt = time.localtime()
print('local time is %s  type is  %s ' % (localt,type(localt)))

#将元组的时间格式转换成字符串格式的时间
print('LocalTime is %s ' % time.strftime('%Y-%m-%d %H:%M:%S',localt))
start = time.time()
count = 0
for cock in range(0,21):
  for hen in range(0,34):
    for chick in range (3,101,3):
      if (cock + hen + chick == 100) and (cock * 5 + hen * 3 + chick /3 == 100):
        print('cock is %d\then is %d\tchick is %d' % (cock, hen, chick))
        count += 1
end = time.time()
print(end - start,end=' --end-start\n')

print("\033[32;40;1mThere are  %d answers\033[0m" % count)
print(datetime.datetime.now())
