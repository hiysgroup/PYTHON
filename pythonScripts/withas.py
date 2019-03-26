#!/usr/bin/env  python3

src_frb = '/usr/bin/ls'
dst_fwb = '/tmp/newls'

src_frb_obj = open(src_frb,'rb')
dst_fwb_obj = open(dst_fwb,'wb')

booleanrun = True
while  booleanrun :
  frbdata = src_frb_obj.read(4096)
  if  frbdata ==  b'':
    booleanrun = False
  dst_fwb_obj.write(frbdata)
else:
  src_frb_obj.close()
  dst_fwb_obj.close()
  print('Normal closure-------')

print('---- with  as  -------')
with open('filex.txt') as fobj:
  data = fobj.readline()
  print(data,end=' ---as--')
print(data,end= " = = = = =\n")

