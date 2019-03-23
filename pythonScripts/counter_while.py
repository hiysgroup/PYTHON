#!/usr/bin/env  python3
import  random
import  getpass

result,counter = 0 , 1
print("result is %s\t counter is %s " % (result,counter))

print(type(result),end=' ---type result')
print(type(counter),end= ' ---type counter')

while  counter <= 4:
  result += counter
  print("new result is %s\t old counter is %s " % (result,counter))
  print("Result is: %s = %s + %s,\t-------Counter  is: %s" % (result,result - counter,counter,counter))
  counter += 1
  print("new  counter is\t"+str(counter),end=' ~~new counter\n')
  print("-------------------------")

print("Result is: "+str(result))
