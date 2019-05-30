import os
import glob

files = glob.glob('./downloads/kim/*')

for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, 'kim' + '{0:d}'.format(i) + fext)
