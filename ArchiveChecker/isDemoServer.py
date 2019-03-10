import os.path
import sys

with open(os.path.join(sys.path[0], 'Configurations.swift'),'r') as f:
   for idx, line in enumerate(f):
       if 'var' in line:
           words =  line.rstrip('\n').split(" ")
           if words[1] == 'isDemoServer' and words[3] == 'true':
               print(f.name + ':' + str(idx + 1) + ': error: Can\'t archive, your are on demo server!!!!! 😱')
               exit(1)
