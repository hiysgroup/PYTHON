#!/usr/bin/env   python3

apdrg = [ 0, 1]
print(" apdrg is ",apdrg)
for  i  in range(4):
  apdrg.append(apdrg[-1] + apdrg[-2])
  print("i  is %d  \t apdrg is " % i,apdrg)
print(apdrg)
print("*#" * 10)

for i in range(1, 6):    # [1, 2, 3,...]
  for j in range(1, i+1):   # i->1:[1], i->2: [1, 2], i->3: [ 1, 2, 3],...
    print("I=%d J=%d" % (i, j), end = '- ')
    print('%s X %s= %s' % (j, i, i*j), end='\t')
  print()
print("**" * 10)
for i in range(1, 10):    # [1, 2, 3,...]
  for j in range(1, i+1):   # i->1:[1], i->2: [1, 2], i->3: [ 1, 2, 3],...
    print('%s X %s= %s' % (j, i, i*j), end='\t')
  print()
