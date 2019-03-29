#!/usr/bin/env  python3
import  keyword, sys, os, getpass
"This  is a test module"
sys.stdout.write('\033[30;43;1m__name__ yellow is %s\n\033[0m' % __name__)

def  get_fname():
  while True:
    filename = input('Please input filename: ')
 #表示判断文件是否存在 os.path.exists(filename)
    if  os.path.exists(filename):
      print('\033[30;41;1m %s already exists\033[0m' % filename)
    else:
      print('\033[31;40;1m %s not exists\033[0m' % filename)
      break
  return filename

def  get_contents():
  contents = []
  sys.stdout.write('\033[29;42;1m Please input content end with end\n\033[0m')
  while True:
    print('input end with end')
#sys.stdin.readline()输入,输出的是"字符串+\n"的形式
    line = sys.stdin.readline()
    if  line == 'end\n':
      break
    contents.append(line)
  return  contents

def  wfile(fname,contents):
  with open(fname,'w') as fobj:
    fobj.writelines(contents)

if __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv[0] is %s red\n\033[0m' % sys.argv[0])
  sys.stdout.write('\033[32;48;1msys.argv is %s \n\033[0m' % sys.argv)
#  print(keyword.kwlist)
#  print(keyword.iskeyword('asxx'))
#  print(keyword.iskeyword('as'))
#  print('pass' in keyword.kwlist)
  fname = get_fname()
  contents = get_contents()
#  contents = ['%s \n' % line for line  in contents]
  wfile(fname,contents)

