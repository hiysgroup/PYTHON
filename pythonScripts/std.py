#!/usr/bin/env  python3
import  sys

sys.stdout.write("Please input your name  --stdout.write\n")
name = sys.stdin.readline().strip('\n')
sys.stdout.write("your name is %s --stdout.write\n" % name)

sys.stderr.write("your name is %s --stderr\n" % name)
