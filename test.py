import os

adb  = 'adb devices'
d = os.system(adb)
print(d)