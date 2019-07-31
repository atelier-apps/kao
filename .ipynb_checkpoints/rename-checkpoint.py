import os
import glob

files = glob.glob('./hyper-test-pics/kim/*')

for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, './/hyper-test-pics/kim/1_kim' + '{0:d}'.format(i) + fext)