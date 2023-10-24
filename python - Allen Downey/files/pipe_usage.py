import os
# popen is deprecated and subprocess should be used
# but for simple demonstrations, it is used here to run shell
# commands in python
cmd = 'dir'
fp = os.popen(cmd)

res = fp.read()
print(res)

stat = fp.close()
print(stat)