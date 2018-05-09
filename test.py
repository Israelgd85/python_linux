#coding: utf-8

__autor__="Israel Gomes Deconto"


import os

output = os.popen('ls')

print(output)

num = output.count('d')
