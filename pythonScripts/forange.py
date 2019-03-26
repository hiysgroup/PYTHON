#!/usr/bin/env   python3

apdrg = [ 0, 1]
print(" apdrg is ",apdrg)
for  i  in range(4):
  apdrg.append(apdrg[-1] + apdrg[-2])
  print("i  is %d  \t apdrg is " % i,apdrg)
print(apdrg)
print("*#" * 10)
a, b = 0, 1
apd = [0]
print("--- apd is ",apd)
for i  in  range(4):
  a, b = b, a + b
  apd.append(a)
  print("i  is %d  \t apd  is " % i,apd)
print(apd)

print("#" * 10)
fib = [ 0, 1 ]
l = int(input("input: "))

for i in range(l-2):
   fib.append(fib[-1] + fib[-2])
print(fib)

