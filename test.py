import __init__
import os
from random import randint

if not os.path.exists('uploads/'):
    os.makedirs('uploads/')
    
f = file("example.txt", "w+")
f.write("this is some text I'm putting here.")
f.close()


for x in range(0,2000):
  temp = randint(0,2000)
  __init__.read_file('uploads/example.txt', temp)
  __init__.search_file(temp)
  __init__.find_number(temp)
  __init__.put_file('uploads/example.txt', temp)
