import time
def slowprint(text):
  text = str(text)
  duration = 0
  while(duration < len(text)): 
    time.sleep(0.1)
    print((text[duration]),end = "", flush = True)
    duration = duration+1
  return 
#Your slowly print sux
from time import sleep
def printslow(_input, delay=0.03):
  for i in range(len(_input):
    print(_input[:i+1],end='\r', flush=True)
    sleep(delay)
 slowprint('FooBar')
 printslow('BarFoo')
